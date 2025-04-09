from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from helper_functions import regular_expression_into_dfa
from helper_functions import check_dfa_equivalence


# regex = input("Entre com a expressão regular: ")

# dfa1 = regular_expression_into_dfa(regex)
# print(dfa1)

# a(a*(ba)*)*
nfa1 = NFA(
    states={"q0", "q1", "q2"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": {"q1"}},
        "q1": {"a": {"q1","q2"}, "b": {"q1"}}
    },
    initial_state="q0",
    final_states={"q2"}
)
dfa2 = DFA.from_nfa(nfa1)
# print(dfa2)
# print(check_dfa_equivalence(dfa1,dfa2))