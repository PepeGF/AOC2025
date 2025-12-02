from read_data import read_data_web, save_data
import sys

data = read_data_web()
save_data(sys.argv[1], data)