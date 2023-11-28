import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="WK9/code/python_logger_output/bp_bs.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

## simple function

def bloodpressure(x, y):
    try:
        total = x + y
        logging.debug(f"success! total is {total}")
        return total
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return "try again"

output1 = bloodpressure(120, 80) # we expect this to give a debug success

output2 = bloodpressure("150", 80) # we expect this to fail

def bloodsugar(x):
    try:
        if x >= 100:
            interpretation = "bad"
            logging.debug(f"success! blood sugar: {interpretation}")
            print(f'interpretation: {interpretation}')
            return interpretation
        else:
            interpretation = "good"
            logging.debug(f"success! blood sugar: {interpretation}")
            print(f'interpretation: {interpretation}')
            return interpretation
    except Exception as e:
        print(e)
        logging.error(f"an error occured! {e}")
        return "try again"
    
boodsugar1 = bloodsugar("100")