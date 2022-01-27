#! /usr/bin/python3

import argparse
import os
import random
import time

def delete_line(fname: str, targetLine: int) -> None:
	try:
		with open(fname, 'r') as file:
			lines = file.readlines()
	except OSError:
		print('File not found')
		exit()

	lines.pop(targetLine)

	with open(fname, 'w') as file:
		file.writelines(lines)


def get_line_count(fname: str) -> int:
	try:
		with open(fname, 'r') as file:
			lines = file.readlines()
	except OSError:
		print('File not found')
		exit()

	return len(lines)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', '-f', type=str, help='file to delete lines from')
	parser.add_argument('--interval', '-i', type=int, help='number of seconds per each deletion', default=60)
	args = parser.parse_args()
	
	fname = args.file
	interval = args.interval

	while True:
		time.sleep(interval)
		lineCount = get_line_count(fname)

		targetLine = random.randint(0, lineCount - 1)
		delete_line(fname, targetLine)

if __name__ == '__main__':
	main()