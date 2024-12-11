def validate_sequence(values, allow_one_error=True):
    def is_valid_sequence(seq, increasing):
        """Check if sequence is valid based on increasing/decreasing flag"""
        for i in range(len(seq) - 1):
            if increasing and seq[i] >= seq[i+1]:
                return False
            if not increasing and seq[i] <= seq[i+1]:
                return False
        return True
    
    def check_adjacent_difference(seq):
        """Check if adjacent differences are at most 3"""
        return all(abs(seq[i] - seq[i+1]) <= 3 for i in range(len(seq) - 1))
    
    # Check if original sequence is valid
    if is_valid_sequence(values, values[0] < values[-1]) and check_adjacent_difference(values):
        return True
    
    # If not allowing errors, return False
    if not allow_one_error:
        return False
    
    # Try removing each element once
    for i in range(len(values)):
        # Create a new sequence without the i-th element
        modified_seq = values[:i] + values[i+1:]
        
        # Check if this modified sequence is valid (both increasing and decreasing)
        if (is_valid_sequence(modified_seq, modified_seq[0] < modified_seq[-1]) and 
            check_adjacent_difference(modified_seq)):
            return True
    
    return False

def main():
    count = 0
    with open('input') as file:
        for line in file:
            nums = [int(x) for x in line.split()]
            
            if validate_sequence(nums):
                count += 1
    
    print(count)

main()
