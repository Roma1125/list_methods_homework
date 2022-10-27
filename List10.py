def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    s=[]
    s.append(list1.count(1))
    s.append(list1.count(0))
    return s
print(main([1,1,1,0,0,0,0,0,0]))