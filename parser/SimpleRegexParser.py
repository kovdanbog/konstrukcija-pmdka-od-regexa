# Generated from SimpleRegex.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,55,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,1,2,1,2,1,2,1,2,
        5,2,29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,44,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,53,8,4,1,4,0,2,2,
        4,5,0,2,4,6,8,0,0,56,0,10,1,0,0,0,2,12,1,0,0,0,4,23,1,0,0,0,6,43,
        1,0,0,0,8,52,1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,0,12,13,6,1,-1,0,13,
        14,3,4,2,0,14,20,1,0,0,0,15,16,10,2,0,0,16,17,5,1,0,0,17,19,3,4,
        2,0,18,15,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,
        1,0,0,0,22,20,1,0,0,0,23,24,6,2,-1,0,24,25,3,6,3,0,25,30,1,0,0,0,
        26,27,10,2,0,0,27,29,3,6,3,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,
        0,0,0,30,31,1,0,0,0,31,5,1,0,0,0,32,30,1,0,0,0,33,34,3,8,4,0,34,
        35,5,2,0,0,35,44,1,0,0,0,36,37,3,8,4,0,37,38,5,3,0,0,38,44,1,0,0,
        0,39,40,3,8,4,0,40,41,5,4,0,0,41,44,1,0,0,0,42,44,3,8,4,0,43,33,
        1,0,0,0,43,36,1,0,0,0,43,39,1,0,0,0,43,42,1,0,0,0,44,7,1,0,0,0,45,
        53,5,7,0,0,46,47,5,5,0,0,47,48,3,0,0,0,48,49,5,6,0,0,49,53,1,0,0,
        0,50,51,5,5,0,0,51,53,5,6,0,0,52,45,1,0,0,0,52,46,1,0,0,0,52,50,
        1,0,0,0,53,9,1,0,0,0,4,20,30,43,52
    ]

class SimpleRegexParser ( Parser ):

    grammarFileName = "SimpleRegex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'?'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CHAR", "WS" ]

    RULE_regex = 0
    RULE_union = 1
    RULE_concat = 2
    RULE_repeat = 3
    RULE_atom = 4

    ruleNames =  [ "regex", "union", "concat", "repeat", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CHAR=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def union(self):
            return self.getTypedRuleContext(SimpleRegexParser.UnionContext,0)


        def getRuleIndex(self):
            return SimpleRegexParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = SimpleRegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.union(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat(self):
            return self.getTypedRuleContext(SimpleRegexParser.ConcatContext,0)


        def union(self):
            return self.getTypedRuleContext(SimpleRegexParser.UnionContext,0)


        def getRuleIndex(self):
            return SimpleRegexParser.RULE_union

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion" ):
                return visitor.visitUnion(self)
            else:
                return visitor.visitChildren(self)



    def union(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleRegexParser.UnionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_union, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.concat(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleRegexParser.UnionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_union)
                    self.state = 15
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 16
                    self.match(SimpleRegexParser.T__0)
                    self.state = 17
                    self.concat(0) 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConcatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repeat(self):
            return self.getTypedRuleContext(SimpleRegexParser.RepeatContext,0)


        def concat(self):
            return self.getTypedRuleContext(SimpleRegexParser.ConcatContext,0)


        def getRuleIndex(self):
            return SimpleRegexParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)



    def concat(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleRegexParser.ConcatContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_concat, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.repeat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleRegexParser.ConcatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concat)
                    self.state = 26
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 27
                    self.repeat() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RepeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(SimpleRegexParser.AtomContext,0)


        def getRuleIndex(self):
            return SimpleRegexParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)




    def repeat(self):

        localctx = SimpleRegexParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repeat)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.atom()
                self.state = 34
                self.match(SimpleRegexParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.atom()
                self.state = 37
                self.match(SimpleRegexParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.atom()
                self.state = 40
                self.match(SimpleRegexParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(SimpleRegexParser.CHAR, 0)

        def regex(self):
            return self.getTypedRuleContext(SimpleRegexParser.RegexContext,0)


        def getRuleIndex(self):
            return SimpleRegexParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SimpleRegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(SimpleRegexParser.CHAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(SimpleRegexParser.T__4)
                self.state = 47
                self.regex()
                self.state = 48
                self.match(SimpleRegexParser.T__5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(SimpleRegexParser.T__4)
                self.state = 51
                self.match(SimpleRegexParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.union_sempred
        self._predicates[2] = self.concat_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def union_sempred(self, localctx:UnionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def concat_sempred(self, localctx:ConcatContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




