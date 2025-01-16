from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import sys



def check_dfa_equivalence(dfa1,dfa2):
    nfa3 = dfa1.union(dfa2)
    return (nfa3 == dfa1) and (nfa3 == dfa2)


def regular_expression_into_dfa(reg_exp):
    symbols = set()
    # for char in reg_exp:
    #     if char.isalnum():
    #         symbols.add(char)
    for char in "ab":
        symbols.add(char)
    nfa1 = NFA.from_regex(reg_exp,input_symbols=symbols)
    dfa1 = DFA.from_nfa(nfa1)
    return dfa1

def parse_file(file_index):
    file_path = sys.argv[file_index]
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()  # Read the file content
            return file_content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def parse_nfa(input_text):
    lines = input_text.strip().split("\n")
   
    states = set()
    input_symbols = set()
    transitions = {}
    initial_state = None
    final_states = set()
    
    for line in lines:
        # line = line.strip()
        # print(line)
        if line.startswith("states:"):
            states = set(line.split(":")[1].strip().split(", "))
        elif line.startswith("input_symbols:"):
            input_symbols = set(line.split(":")[1].strip().split(", "))
        elif line.startswith("transitions:"):
            # Start reading transitions in subsequent lines
            transitions = {}
            continue
        elif line.startswith(" "):  # Transition lines
            state, rest = line.strip().split(":")
            state = state.strip()
            rest = rest.strip() # a -> q1, q2
           
            symbol,endStates = rest.split("->")
            symbol = symbol.strip()
            if not state in transitions:
                transitions[state] = dict()
            if not symbol in transitions[state]:
                transitions[state][symbol] = set()
            endStates = endStates.strip().split(",")
            for endState in endStates:
                transitions[state][symbol].add(endState.strip())
                # transitions[state].update({symbol:endState})

            
        elif line.startswith("initial_state:"):
            initial_state = line.split(":")[1].strip()
        elif line.startswith("final_states:"):
            final_states = set(line.split(":")[1].strip().split(", "))
    # Create and return the NFA object
    return NFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

def write_dfa_to_file(dfa, output_file):
    with open(output_file, "w") as file:
        file.write("DFA Details\n")
        file.write("===========\n\n")
        
        # Write states
        file.write("States:\n")
        file.write(f"{', '.join(map(str, dfa.states))}\n\n")
        
        # Write input symbols
        file.write("Input Symbols:\n")
        file.write(f"{', '.join(dfa.input_symbols)}\n\n")
        
        # Write transitions
        file.write("Transitions:\n")
        for state, transitions in dfa.transitions.items():
            file.write(f"  From state {state}:\n")
            for symbol, target_state in transitions.items():
                file.write(f"    {symbol} -> {target_state}\n")
        file.write("\n")
        
        # Write initial state
        file.write("Initial State:\n")
        file.write(f"{dfa.initial_state}\n\n")
        
        # Write final states
        file.write("Final States:\n")
        file.write(f"{', '.join(map(str, dfa.final_states))}\n\n")
        
        # Write allow_partial
        # file.write("Allow Partial:\n")
        # file.write(f"{dfa.allow_partial}\n")