import pandas as pd

df = pd.read_csv("test_data.csv")


print("═" * 40)
print("  Test Results Analysis")
print("═" * 40)
print(f"Total tests: {len(df)}")
print(f"Column names and Types: {df.dtypes}")

print("\nFirst 5 rows:")
print(df.head(5)) 
#Calculate aggregate metrics:
total_tests = len(df)
passed_tests = len(df[df["status"] == "PASS"])
pass_rate = (passed_tests / total_tests) * 100
avg_duration_ms = df["duration_ms"].mean()
avg_duration_sec = avg_duration_ms / 1000 #Convert ms to seconds
slowest_test = df.loc[df["duration_ms"].idxmax()]
fastest_test = df.loc[df["duration_ms"].idxmin()]

print("\nAggregate Metrics:")
print(f"Passed: {passed_tests}")
print(f"Pass Rate: {pass_rate:.1f}%")
print(f"Average Duration: {avg_duration_sec:.2f} seconds")
print(f"Slowest Test: {slowest_test['name']} ({slowest_test['duration_ms']} ms)")
print(f"Fastest Test: {fastest_test['name']} ({fastest_test['duration_ms']} ms)")

#Group by module
print("-- By Module --")
module_stats = df.groupby("module").agg(
    tests=("name", "count"),
    avg_duration=("duration_ms", "mean"),
    num_tests=("name", "count"),
)







#Pass rate per module
#Average duration per module
#Number of tests per module
#Filter and display:

#All failed tests (name, module, duration)
#Tests slower than 1500ms
#Tests in the "auth" module
#Add a computed column:

#duration_sec = duration_ms / 1000
#Sort and export:

#Sort by duration (descending)
#Save the result to output/results_sorted.csv