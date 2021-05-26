import scipy.stats
import pickle
import matplotlib.pyplot as plt
import sys


# Load data
with open("image_data.bin", "rb") as f:
	data = pickle.load(f)

# Print results
print("The result of the two sample t-test for ASD vs TD: {}".format(scipy.stats.ttest_ind(data["asd_var"], data["td_var"])))
print("-" * 20)
print("The result of the SRCC for ASD on mean image brightness: {}".format(scipy.stats.spearmanr(data["asd_var"], data["im_brightness"])))
print("The result of the SRCC for TD on mean image brightness: {}".format(scipy.stats.spearmanr(data["td_var"], data["im_brightness"])))
print("-" * 20)
print("The result of the SRCC for ASD on variance of image brightness: {}".format(scipy.stats.spearmanr(data["asd_var"], data["im_var"])))
print("The result of the SRCC for TD on variance of image brightness: {}".format(scipy.stats.spearmanr(data["td_var"], data["im_var"])))

# Show graphs
# Choose a graph
plt.xlabel("Weighted Variance of Fixmap")
if len(sys.argv) < 2:
	print("No graph.")
elif sys.argv[1] == "tdb":
	plt.title("TD")
	plt.ylabel("Mean Brightness of Image")
	plt.plot(data["td_var"], data["im_brightness"], "o")
elif sys.argv[1] == "tdv":
	plt.title("TD")
	plt.ylabel("Variance of Brightness of Image")
	plt.plot(data["td_var"], data["im_var"], "o")
elif sys.argv[1] == "asdb":
	plt.title("ASD")
	plt.ylabel("Mean Brightness of Image")
	plt.plot(data["asd_var"], data["im_brightness"], "o")
elif sys.argv[1] == "asdv":
	plt.title("ASD")
	plt.ylabel("Variance of Brightness of Image")
	plt.plot(data["asd_var"], data["im_var"], "o")
elif sys.argv[1] == "td":
	plt.title("TD")
	plt.hist(data["td_var"], 50)
elif sys.argv[1] == "asd":
	plt.title("ASD")
	plt.hist(data["asd_var"], 50)
elif sys.argv[1] == "combined":
	plt.title("ASD and TD")
	_, _, asd_hist = plt.hist(data["asd_var"], 50, alpha=0.5)
	_, _, td_hist = plt.hist(data["td_var"], 50, alpha=0.5)
	plt.legend(handles=[asd_hist, td_hist], labels=["ASD", "TD"])
elif sys.argv[1] == "b":
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
	ax1.set_title("TD")
	ax1.set_ylabel("Mean Brightness of Image")
	ax1.set_xlabel("Weighted Variance of Fixmap")
	ax1.plot(data["td_var"], data["im_brightness"], "o")
	ax2.set_title("ASD")
	ax2.set_ylabel("Mean Brightness of Image")
	ax2.set_xlabel("Weighted Variance of Fixmap")
	ax2.plot(data["asd_var"], data["im_brightness"], "o")
elif sys.argv[1] == "v":
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
	ax1.set_title("TD")
	ax1.set_ylabel("Variance of Brightness of Image")
	ax1.set_xlabel("Weighted Variance of Fixmap")
	ax1.plot(data["td_var"], data["im_var"], "o")
	ax2.set_title("ASD")
	ax2.set_ylabel("Variance of Brightness of Image")
	ax2.set_xlabel("Weighted Variance of Fixmap")
	ax2.plot(data["asd_var"], data["im_var"], "o")

plt.show()

