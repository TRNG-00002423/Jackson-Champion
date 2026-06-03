import pandas as pd

df = pd.read_csv("test_data.csv")


print("═" * 40)
print("  Test Results Analysis")
print("═" * 40)

print("\nFirst 5 rows:")
print(df.head(5)) 
#Calculate aggregate metrics:
total_tests = len(df)
passed_tests = len(df[df["status"] == "pass"])
pass_rate = (passed_tests / total_tests) * 100
avg_duration_ms = df["duration_ms"].mean()
avg_duration_sec = avg_duration_ms / 1000 #Convert ms to seconds
slowest_test = df.loc[df["duration_ms"].idxmax()]
fastest_test = df.loc[df["duration_ms"].idxmin()]

print("\nAggregate Metrics:")
print(f"Total tests: {len(df)}")
print(f"Pass Rate: {pass_rate:.1f}%")
print(f"Average Duration: {avg_duration_sec:.2f} seconds")
print(f"Slowest Test: {slowest_test['test_name']} ({slowest_test['duration_ms']} ms)")
print(f"Fastest Test: {fastest_test['test_name']} ({fastest_test['duration_ms']} ms)")

#Group by module
print("-- By Module --")
module_stats = df.groupby("module").agg(
    tests=("test_name", "count"),
    passed=("status", lambda x: (x == "pass").sum()),
    avg_duration=("duration_ms", "mean")
)

module_stats["pass_rate"] = (module_stats["passed"] / module_stats["tests"]) * 100


module_stats["pass_rate"] = (module_stats["passed"] / module_stats["tests"]) * 100
print(module_stats[["tests", "pass_rate", "avg_duration"]])

print("\n-- Failed Tests --")
failed = df[df["status"] == "FAIL"]
print(failed[["test_name", "module", "duration_ms"]])

print("\n-- Tests Slower Than 1500ms --")
slow_tests = df[df["duration_ms"] > 1500]
print(slow_tests[["test_name", "module", "duration_ms"]])

print("\n-- Auth Module Tests --")
auth_tests = df[df["module"] == "auth"]
print(auth_tests[["test_name", "status", "duration_ms"]])

df["duration_sec"] = df["duration_ms"] / 1000

df_sorted = df.sort_values(by="duration_ms", ascending=False)
df_sorted.to_csv("results_sorted.csv", index=False)




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