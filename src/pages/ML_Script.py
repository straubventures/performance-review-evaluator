import gensim

def getAverage(text_input):
    word = ""
    array = []
    for letter in text_input:
        if letter == " " or letter == '.':
            array.append(word)
            word = ""
        else:
            word = word + letter
    return array

def prediction_model(string_input):

    print("starting...")
    model = gensim.models.KeyedVectors.load_word2vec_format('/Users/straubfamily/cleanProj/try2Django/src/pages/'
                                                            'GoogleNews-vectors-negative300.bin', binary=True)
    print("this is done")

    arr = getAverage(string_input)

    print(arr)
    rangeArr = []
    final_arr = []
    for word in arr:
        if word not in model:
            continue
        final_arr.append([str(word), 0.0])
        list = model.similar_by_word(word, topn=50)
        min = ['', 1000.0]
        max = ['', 0.0]
        for value in list:
            if value[1] < min[1]:
                min = value
            if value[1] > max[1]:
                max = value

        range = max[1] - min[1]
        rangeArr.append(range)

    print(rangeArr)

    average = 0
    for i, num in enumerate(rangeArr):
        final_arr[i][1] = num
        average = average + num

    average = average / len(rangeArr)

    for number in rangeArr:
        average = average + (.005)

    answer_array = [average, final_arr]

    return answer_array


