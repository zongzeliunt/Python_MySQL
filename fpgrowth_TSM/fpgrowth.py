import pyfpgrowth
import os


transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]

folder_name = "TSM_main_folder/test_log_folder_2/"


def get_transactions_from_folder (folder_name):
	file_list = []
	for filename in os.listdir (folder_name):
		file_path_name = folder_name
		file_list.append(folder_name + filename)

	print file_list

	transactions = []

	for block_report_file in file_list:
		print block_report_file
		fl = open(block_report_file, "r")
		node_block_lines = fl.readlines()
		node_block_report = []
		for line in node_block_lines:
			
			block_name = line.split()[0]
			
			block_name_list = block_name.split("_")
			block_type = block_name_list[0]
			block_num = int(block_name_list[1])
			if block_type == "block":
				node_block_report.append("message_" + str(1000 + block_num))
			else:
				node_block_report.append(block_name)
			



		transactions.append(node_block_report)
		fl.close()



	return transactions



transactions = get_transactions_from_folder (folder_name)
print transactions



patterns = pyfpgrowth.find_frequent_patterns(transactions, 3)

patterns_file = "patterns_file.txt"
fl = open(patterns_file, "w")
for pattern in patterns:
	fl.write(str(pattern) + "\n") 


fl.close()

rules = pyfpgrowth.generate_association_rules(patterns, 1.0)

print "rules"
print rules
