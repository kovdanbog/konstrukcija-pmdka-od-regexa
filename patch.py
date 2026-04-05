from visual_automata.fa.nfa import VisualNFA
from visual_automata.fa.nfa import Digraph
from visual_automata.fa.nfa import hex_to_rgb_color
from visual_automata.fa.nfa import create_palette
from visual_automata.fa.nfa import list_cycler
from visual_automata.fa.nfa import sRGBColor
from visual_automata.fa.nfa import display


# Funkcija modifikuje funkciju transitions_pairs iz biblioteke visual_automata, tako sto forsira kastovanje prelaza u skup
def bezbedan_transitions_pairs(all_transitions):
    all_transitions = all_transitions.deepcopy()
    transition_possibilities = []

    for state, state_transitions in all_transitions.items():
        for symbol, transitions in state_transitions.items():

            if isinstance(transitions, frozenset):
                transitions = set(transitions)

            if len(transitions) < 2:
                if transitions != "" and transitions != {}:
                    transitions = next(iter(transitions))
                transition_possibilities.append((state, transitions, symbol))
            else:
                for transition in transitions:
                    transition_possibilities.append((state, transition, symbol))

    return transition_possibilities

# Ostatak je samo zamena originalnog λ simbola za praznu rec sa ε
def _add_epsilon(all_transitions: dict, input_symbols: str) -> dict:
        
    all_transitions = all_transitions.deepcopy()
    input_symbols = input_symbols.copy()
       
    for transitions in all_transitions.values():
        for state, transition in list(transitions.items()):
            if state == "":
                transitions["ε"] = transition
                del transitions[""]
                input_symbols.add("ε")

    return all_transitions

def epsilon_show_diagram(
        self,
        input_str: str = None,
        filename: str = None,
        format_type: str = "png",
        path: str = None,
        *,
        view=False,
        cleanup: bool = True,
        horizontal: bool = True,
        reverse_orientation: bool = False,
        fig_size: tuple = (8, 8),
        font_size: float = 14.0,
        arrow_size: float = 0.85,
        state_seperation: float = 0.5,
    ) -> Digraph:  
        fig_size = ", ".join(map(str, fig_size))
        font_size = str(font_size)
        arrow_size = str(arrow_size)
        state_seperation = str(state_seperation)

        # Defining the graph.
        graph = Digraph(strict=False)
        graph.attr(
            size=fig_size,
            ranksep=state_seperation,
        )
        if horizontal:
            graph.attr(rankdir="LR")
        if reverse_orientation:
            if horizontal:
                graph.attr(rankdir="RL")
            else:
                graph.attr(rankdir="BT")

        # Defining arrow to indicate the initial state.
        graph.node("Initial", label="", shape="point", fontsize=font_size)

        # Defining all states.
        for state in sorted(self.nfa.states):
            if (
                state in self.nfa.initial_state
                and state in self.nfa.final_states
            ):
                graph.node(state, shape="doublecircle", fontsize=font_size)
            elif state in self.nfa.initial_state:
                graph.node(state, shape="circle", fontsize=font_size)
            elif state in self.nfa.final_states:
                graph.node(state, shape="doublecircle", fontsize=font_size)
            else:
                graph.node(state, shape="circle", fontsize=font_size)

        # Point initial arrow to the initial state.
        graph.edge("Initial", self.nfa.initial_state, arrowsize=arrow_size)

        # Define all tansitions in the finite state machine.
        all_transitions_pairs = self._transitions_pairs(self.nfa.transitions)

        # Replacing '' key name for empty string (lambda/epsilon) transitions.
        for i, pair in enumerate(all_transitions_pairs):
            if pair[2] == "":
                all_transitions_pairs[i] = (pair[0], pair[1], "ε")

        if input_str is None:
            for pair in all_transitions_pairs:
                graph.edge(
                    pair[0],
                    pair[1],
                    label=" {} ".format(pair[2]),
                    arrowsize=arrow_size,
                    fontsize=font_size,
                )
            status = None

        else:
            (
                status,
                taken_transitions_pairs,
                taken_steps,
                inputs,
            ) = self.input_check(input_str=input_str, return_result=True)
            if not isinstance(status, bool):
                print(status)
                return

            remaining_transitions_pairs = [
                x
                for x in all_transitions_pairs
                if x not in taken_transitions_pairs
            ]

            # Define color palette for transitions
            if status:
                start_color = hex_to_rgb_color("#FFFF00")
                end_color = hex_to_rgb_color("#00FF00")
            else:
                start_color = hex_to_rgb_color("#FFFF00")
                end_color = hex_to_rgb_color("#FF0000")
            number_of_colors = len(inputs)
            palette = create_palette(
                start_color, end_color, number_of_colors, sRGBColor
            )
            color_gen = list_cycler(palette)

            # Define all tansitions in the finite state machine with traversal.
            counter = 0
            for i, pair in enumerate(taken_transitions_pairs):
                dead_state = "\u00D8"
                edge_color = next(color_gen)
                counter += 1
                if pair[1] != {}:
                    graph.edge(
                        pair[0],
                        pair[1],
                        label=" [{}]\n{} ".format(counter, pair[2]),
                        arrowsize=arrow_size,
                        fontsize=font_size,
                        color=edge_color,
                        penwidth="2.5",
                    )
                else:
                    graph.node(dead_state, shape="circle", fontsize=font_size)
                    graph.edge(
                        pair[0],
                        dead_state,
                        label=" [{}]\n{} ".format(counter, inputs[-1]),
                        arrowsize=arrow_size,
                        fontsize=font_size,
                        color=edge_color,
                        penwidth="2.5",
                    )

            for pair in remaining_transitions_pairs:
                graph.edge(
                    pair[0],
                    pair[1],
                    label=" {} ".format(pair[2]),
                    arrowsize=arrow_size,
                    fontsize=font_size,
                )

        # Write diagram to file. PNG, SVG, etc.
        if filename:
            graph.render(
                filename=filename,
                format=format_type,
                directory=path,
                cleanup=cleanup,
            )

        if view:
            graph.render(view=True)
        if input_str:
            display(taken_steps)
            return graph
        else:
            return graph

VisualNFA._transitions_pairs = staticmethod(bezbedan_transitions_pairs)
VisualNFA._add_lambda = staticmethod(_add_epsilon)
VisualNFA.show_diagram = epsilon_show_diagram
