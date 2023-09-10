#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        for i in range(len(my_list)):
            if (idx < 0) or (idx > len(my_list)):
                return (None)
            elif (idx == i):
                return (my_list(i))
