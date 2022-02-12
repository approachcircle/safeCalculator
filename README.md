<!-- markdownlint-disable MD033 -->
# safeCalculator

this is a calculator that evaluates expressions using polish notation, so + 1 2 is polish notation for 1 + 2. here a wikipedia article to explain polish notation can be found <a href="https://en.wikipedia.org/wiki/Polish_notation">here</a>.

## what makes this calculator 'safe'?

this calculator has primitive, operator-specific restrictions on how big operands can be. in english terms, this means that calculations that would be quite memory expensive are prevented from being executed unless the 'unsafe' variable is true.

## how big can operands be in safe mode?

the limit for how big operands can be varies from operator to operator. for example, the biggest operand that a factorial calculation can be is significantly smaller than the biggest operand for an addition calculation, due to the fact that factorial calculations are a lot more memory intensive. you can find the maximum operand size for any calculation in "main.py"; it should be located in a separate class which is dedicated to storing global variables.

## how big can operands be in unsafe mode then?

the limit to how big operands can be in unsafe mode is however much memory windows has allowed python to hog.

## how do i toggle between safe and unsafe mode?

you can toggle between the two by executing the command "#unsafe", and the program will output either: "unsafe = False -> True" or "unsafe = True -> False" respectively.

## why are expressions evaluated following polish mathematical notation?

because it's a lot easier to parse and evaluate than EMN (english mathematical notation). for a more detailed explanation: PMN (polish mathematical notation) is always preceded by the active operator first, so the program is able to identify what operator we are going to be working with immediately. after the operator is identified, we are provided with a nice space separated list of operands to apply the operator to, which we can easily tokenize, and then evaluate. using PMN to tokenize and evaluate statements is much simpler to the contrary, where we would be given the first operand without knowing what to do with it, followed by the operator, and then followed by the second operand, which requires much more work to tokenize and evaluate.

## symbol lookup table

| symbol | where/how does it occur |
|--------|-------------------------|
| ~ | this symbol indicates that an error has occurred in the last expression. it may occur if an incorrect operand is entered |
| Ω | this symbol indicates that a number is too big/too small to work with. it occurs when too big/too small of an operand is entered while the program is in safe mode |
| OK | this indicates that an expression has been evaluated successfully (to the program's knowledge at least) |

## symbol combination lookup table

| combination | what it means |
|-------------|-----|
| n OK | (let n represent any number) this is the most common combination you will encounter. n is the result of the last expression, and OK shows that the expression completed successfully.
| 0 ~ | this is the second most common combination you may encounter. the zero represents what the program has returned, and the tilde represents that an error has occurred. |
| Ω ~ | this is also a relatively common combination to encounter. it means that you have entered an operand that was too big or too small to be calculated with in safe mode. you must toggle safe mode to work with an operand of this magnitude.
| None ~ | this is probably the most uncommon combination to encounter. 'None' represents python's null literal, being displayed as a string, and once again, the tilde just shows that an error has occurred. i have no idea how you would go about achieving this combination, but it may happen in a very rare scenario, hence why i have included it.|
