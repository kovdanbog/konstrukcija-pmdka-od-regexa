# Generated from SimpleRegex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleRegexParser import SimpleRegexParser
else:
    from SimpleRegexParser import SimpleRegexParser

# This class defines a complete generic visitor for a parse tree produced by SimpleRegexParser.

class SimpleRegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleRegexParser#regex.
    def visitRegex(self, ctx:SimpleRegexParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleRegexParser#union.
    def visitUnion(self, ctx:SimpleRegexParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleRegexParser#concat.
    def visitConcat(self, ctx:SimpleRegexParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleRegexParser#repeat.
    def visitRepeat(self, ctx:SimpleRegexParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleRegexParser#atom.
    def visitAtom(self, ctx:SimpleRegexParser.AtomContext):
        return self.visitChildren(ctx)



del SimpleRegexParser