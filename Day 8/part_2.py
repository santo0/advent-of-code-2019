import numpy as np

def get_transposing_pixels(all_layers, wide, tall):
    num_of_layers = len(all_layers)
    final_image = [2 for i in range(wide * tall)]
    # change value of
    count_changes = 0
    for j in range(wide*tall):
        for i in range(num_of_layers):
            if final_image[j] == 2:
                final_image[j] = all_layers[i][j]
                count_changes += 1
    print(count_changes)
    return final_image

def get_result(transposed_pixels, wide, tall):
    digits = [d for d in transposed_pixels]
    array = np.array(digits).reshape(tall, wide)
    print(array)
    