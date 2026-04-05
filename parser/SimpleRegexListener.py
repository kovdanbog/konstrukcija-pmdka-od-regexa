# Generated from SimpleRegex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleRegexParser import SimpleRegexParser
else:
    from SimpleRegexParser import SimpleRegexParser

# This class defines a complete listener for a parse tree produced by SimpleRegexParser.
class SimpleRegexListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleRegexParser#regex.
    def enterRegex(self, ctx:SimpleRegexParser.RegexContext):
        pass

    # Exit a parse tree produced by SimpleRegexParser#regex.
    def exitRegex(self, ctx:SimpleRegexParser.RegexContext):
        pass


    # Enter a parse tree produced by SimpleRegexParser#union.
    def enterUnion(self, ctx:SimpleRegexParser.UnionContext):
        pass

    # Exit a parse tree produced by SimpleRegexParser#union.
    def exitUnion(self, ctx:SimpleRegexParser.UnionContext):
        pass


    # Enter a parse tree produced by SimpleRegexParser#concat.
    def enterConcat(self, ctx:SimpleRegexParser.ConcatContext):
        pass

    # Exit a parse tree produced by SimpleRegexParser#concat.
    def exitConcat(self, ctx:SimpleRegexParser.ConcatContext):
        pass


    # Enter a parse tree produced by SimpleRegexParser#repeat.
    def enterRepeat(self, ctx:SimpleRegexParser.RepeatContext):
        pass

    # Exit a parse tree produced by SimpleRegexParser#repeat.
    def exitRepeat(self, ctx:SimpleRegexParser.RepeatContext):
        pass


    # Enter a parse tree produced by SimpleRegexParser#atom.
    def enterAtom(self, ctx:SimpleRegexParser.AtomContext):
        pass

    # Exit a parse tree produced by SimpleRegexParser#atom.
    def exitAtom(self, ctx:SimpleRegexParser.AtomContext):
        pass



del SimpleRegexParser