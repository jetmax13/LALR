from parsing import *
import samples
import firstfollow
from firstfollow import *


def get_grammar():
    return samples.get_sample_1()


def describe_grammar(gr):
    return '\n'.join([
        'Indexed grammar rules (%d in total):' % len(gr.productions),
        str(gr) + '\n',
        'Grammar non-terminals (%d in total):' % len(gr.nonterms),
        '\n'.join('\t' + str(s) for s in gr.nonterms) + '\n',
        'Grammar terminals (%d in total):' % len(gr.terminals),
        '\n'.join('\t' + str(s) for s in gr.terminals)
    ])


def describe_parsing_table(table):
    conflict_status = table.get_conflict_status()

    def conflict_status_str(state_id):
        has_sr_conflict = (conflict_status[state_id] == lalr_one.STATUS_SR_CONFLICT)
        status_str = ('shift-reduce' if has_sr_conflict else 'reduce-reduce')
        return 'State %d has a %s conflict' % (state_id, status_str)

    return ''.join([
        'PARSING TABLE SUMMARY\n',
        'Is the given grammar LALR(1)? %s\n' % ('Yes' if table.is_lalr_one() else 'No'),
        ''.join(conflict_status_str(sid) + '\n' for sid in range(table.n_states)
                if conflict_status[sid] != lalr_one.STATUS_OK) + '\n',
        table.stringify()
    ])


def main(input_file):
  
    
    firstfollow.main(input_file)
    
    
    global production_list, ntl, nt_list, tl, t_list    

   

    print("\tFIRST AND FOLLOW OF NON-TERMINALS")
    for nt in nt_list:
        firstfollow.compute_first(nt)
        firstfollow.compute_follow(nt)
        print(nt)
        print("\tFirst:\t", firstfollow.get_first(nt))
        print("\tFollow:\t", firstfollow.get_follow(nt), "\n")
    
    gr = get_grammar()
    table = lalr_one.ParsingTable(gr)
    

    output_filename = 'parsing-table'

    table.save_to_csv(output_filename + '.csv')
    

    return production_list



if __name__ == "__main__":
    input_file = 'sample1.txt'
    main(input_file)
