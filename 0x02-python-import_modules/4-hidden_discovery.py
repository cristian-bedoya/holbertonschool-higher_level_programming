#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for file_ in dir(hidden_4):
        if file_[0:2] != "__":
            print(file_)
