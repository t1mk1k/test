#!/usr/bin/python

import argparse


if __name__ == '__main__':
    '''
    script for preprocessing books and extracting valence
    example use: python run.py -i './data/raw/' -o './data/emotion_data' -t './data/tmp'
    
    '''
    print("Starting Python script in workspace")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', help='input folder', required=True)
    parser.add_argument('-o', '--output_path', help='output folder', required=True)
    parser.add_argument('-t', '--temp', help='temp folder', required=True)
    
    args = parser.parse_args()
    
    data_file_path = f"{args.input_path}/words.txt"
    results_file_path = f"{args.output_path}/results.txt"
    
    print(f"data_file_path: {data_file_path}")
    print(f"results_file_path: {results_file_path}")
    
    with open(data_file_path, "r") as data_file:
      data = data_file.read()
      words = data.split()

    average_word_length = reduce(lambda x, y: x+y, words, 0) / float(len(words))

    print(f"Number of words: {len(words)}")
    print(f"Average word length is {average_word_length}")
        
    with open(results_file_path, "w") as results_file:
      results_file.write(f"Average word length is {average_word_length}")
