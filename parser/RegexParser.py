from antlr4 import *
from .SimpleRegexLexer import SimpleRegexLexer
from .SimpleRegexParser import SimpleRegexParser
from .SimpleRegexVisitor import SimpleRegexVisitor

class ASTBuilder(SimpleRegexVisitor):
    def visitRegex(self, ctx):
        return self.visit(ctx.union())

    # union : union '|' concat | concat
    def visitUnion(self, ctx):
        # Case: union → concat
        if ctx.union() is None:
            return self.visit(ctx.concat())

        # Case: union → union '|' concat
        left = self.visit(ctx.union())
        right = self.visit(ctx.concat())

        return ("union", left, right)

    # concat : concat repeat | repeat
    def visitConcat(self, ctx):
        # Case: concat → repeat
        if ctx.concat() is None:
            return self.visit(ctx.repeat())

        # Case: concat → concat repeat
        left = self.visit(ctx.concat())
        right = self.visit(ctx.repeat())

        return ("concat", left, right)

    # repeat : atom '*' | atom '+' | atom '?' | atom
    def visitRepeat(self, ctx):
        atom_node = self.visit(ctx.atom())
        if ctx.getChildCount() == 2:   # atom '*' | atom '+' | atom '?'
            op = ctx.getChild(1).getText()

            if op == '*':
                return ("star", atom_node)
            elif op == '+':
                return ("plus", atom_node)
            elif op == '?':
                return ("optional", atom_node)
            
        return atom_node # atom

    # atom : CHAR | '(' regex ')' | '(' ')'
    def visitAtom(self, ctx):
    
        # CHAR
        if ctx.CHAR():
            return ("char", ctx.CHAR().getText())

        # ()
        if ctx.getChildCount() == 2:
            return ("char", None)   # epsilon

        # (regex)
        return self.visit(ctx.regex())

def parse_regex(regex):
    lexer = SimpleRegexLexer(InputStream(regex))
    tokens = CommonTokenStream(lexer)
    parser = SimpleRegexParser(tokens)
    tree = parser.regex()

    # Transform parse tree into AST
    ast = ASTBuilder().visit(tree)

    return ast
