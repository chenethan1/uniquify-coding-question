# this is where you enter the data and shape for the problem
data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, 10, 42, 7, 12, 41, 33, 34, 35, 36, 40, 48]
shape0 = [3, 2, 3]


# this function is here to determine the number of values you want to keep in the data list
def multiply(shape):
    shape_values = 1  # set the base value to 1 so multiplying the values in shape is possible
    for number in shape:
        shape_values *= number  # for each number in shape, will loop until all values are multiplied
    return shape_values  # returns the final product


# this function is here to adjust the data so that it will match the shape_values number
def adjust_data(data, shape):
    shape_values = multiply(shape)  # call shape_values from the multiply function
    adjusted_data = data  # create adjusted_data for the list to be the correct length
    if len(data) < shape_values:
        padding = [0] * (shape_values - len(data))
        adjusted_data = data + padding  # if the data length < shape_values product, add 0's until enough values
    elif len(data) > shape_values:
        adjusted_data = data[:shape_values]
        # if the data length > shape_values product, only take the values from shape_values and before
    return adjusted_data  # return the new adjusted_data which has the correct length of shape_values


# this function is here to create a sublist from the data
def recursive_data(data, shape):
    if len(shape) == 0:  # if the shape given is an empty list, return an empty list
        return []
    if len(shape) == 1:  # if the length of shape is 1, then the data doesn't need to be split more, so return data
        return data
    else:
        dimension = shape[0]  # sets dimension to the next value in shape
        shaped_data = reshape_data(data, dimension)  # calls reshape_data and sets it to shaped_data
        output = []  # creates an empty list for the sublist
        for i in range(dimension):  # this loop goes through the values from 0 to dimension
            sublist = shaped_data[i]  # adds the ith value of shaped_data to the sublist
            reshaped_data = recursive_data(sublist, shape[1:])
            # calls recursive_data to separate the sublist into more sublists
            # removes the first element from shape to pass the rest of the elements through
            output.append(reshaped_data)  # appends the reshaped_data to the initially empty list
        return output  # returns the sublist


# this function is the starting point of the splitting process
def shape_data(data, shape):
    adjusted_data = adjust_data(data, shape)  # call adjusted_data from the adjust_data function
    return recursive_data(adjusted_data, shape)  # calls back to the recursive_data function


'''this function is here to split the data into sublists
dimension is the number of groups the list is being split into'''


def reshape_data(data, dimension):
    step = int(len(data) / dimension)  # sets step to the quotient of the length of the data divided by the dimension
    output = []  # creates another empty list for the sublist
    for index in range(0, len(data), step):  # splits the data into segments of step
        sublist = data[index:index + step]  # creates a sublist with the data from the index to index + step
        output.append(sublist)  # appends that sublist to the output
    return output
    # return [data[index:index+step] for index in range(0, len(data), step)]


print(shape_data(data0, shape0))
