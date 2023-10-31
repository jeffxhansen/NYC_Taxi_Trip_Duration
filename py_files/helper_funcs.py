from config import (
    NP_FLOAT_PRECISION,
    NP_FLOAT_PRECISION_F,
    PD_FLOAT_PRECISION,
    PD_FLOAT_PRECISION_F,
    PD_MAX_COLUMNS,
    PD_MAX_ROWS
)
from time import perf_counter


def set_np_pd_display_params(np, pd):
    """sets numpy and pandas display properties"""
    # sets numpy to avoid scientific and only round to the nth decimal
    np.set_printoptions(precision=NP_FLOAT_PRECISION, suppress=True)
    np.set_printoptions(formatter={'float': NP_FLOAT_PRECISION_F})

    # sets pandas to avoid scientific and only round to the nth decimal
    pd.set_option("display.precision", PD_FLOAT_PRECISION)
    pd.set_option('display.float_format', PD_FLOAT_PRECISION_F)

    # sets pandas to show all columns and rows
    pd.set_option('display.max_columns', PD_MAX_COLUMNS)
    pd.set_option('display.max_rows', PD_MAX_ROWS)
    
    
print_time_p = 0
def p(string=None):
    """a quick and efficient way to have print updates that keeps track of time
    
    Example:
    p("running this function")
    f(*args, **kwargs)
    p()
    
    will print:
    running this function...DONE 0.123 se
    """
    global print_time_p
    if string is not None:
        print(f"{string}...", end="")
        print_time_p = perf_counter()
    else:
        print("DONE", round(perf_counter() - print_time_p, 3), "sec")
        

def movecol(df, cols_to_move=[], ref_col='', place='After'):
    """Moves columns around in a dtaframe
    Examples:
    1)
        df cols ['A', 'B', 'C', 'D', 'X', 'Y', 'Z']
        movecol(df, cols_to_move=['X', 'Y', 'Z'], ref_col='B', place='After')
        df cols ['A', 'B', 'X', 'Y', 'Z', 'C', 'D']]
        
    2)
        df cols ['A', 'B', 'C', 'D', 'X', 'Y', 'Z']
        movecol(df, cols_to_move=['X', 'Y', 'Z'], ref_col='A', place='Before')
        df cols ['X', 'Y', 'Z', 'A', 'B', 'C', 'D']
    """
    cols = df.columns.tolist()
    if place == 'After':
        seg1 = cols[:list(cols).index(ref_col) + 1]
        seg2 = cols_to_move
    if place == 'Before':
        seg1 = cols[:list(cols).index(ref_col)]
        seg2 = cols_to_move + [ref_col]
    seg1 = [i for i in seg1 if i not in seg2]
    seg3 = [i for i in cols if i not in seg1 + seg2]
    return(df[seg1 + seg2 + seg3])
    