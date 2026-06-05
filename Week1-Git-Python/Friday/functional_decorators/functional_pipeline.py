from functools import reduce

test_results = [
    {"name": "test_login", "module": "auth", "duration_ms": 1200, "status": "pass"},
    {"name": "test_register", "module": "auth", "duration_ms": 2100, "status": "pass"},
    {"name": "test_logout", "module": "auth", "duration_ms": 300, "status": "pass"},
    {"name": "test_search", "module": "search", "duration_ms": 850, "status": "fail"},
    {"name": "test_filter", "module": "search", "duration_ms": 1800, "status": "fail"},
    {"name": "test_sort", "module": "search", "duration_ms": 670, "status": "pass"},
    {"name": "test_add_cart", "module": "checkout", "duration_ms": 2300, "status": "fail"},
    {"name": "test_payment", "module": "checkout", "duration_ms": 3100, "status": "pass"},
    {"name": "test_confirm", "module": "checkout", "duration_ms": 1900, "status": "pass"},
    {"name": "test_view_profile", "module": "profile", "duration_ms": 380, "status": "pass"},
    {"name": "test_edit_profile", "module": "profile", "duration_ms": 540, "status": "pass"},
    {"name": "test_settings", "module": "profile", "duration_ms": 420, "status": "fail"},
]

#------Lambda and Sorting------
#sort ascending
sort_ascending = sorted(test_results, key=lambda u: u["duration_ms"])

#Sort module name then duration
sort_module_duration = sorted(test_results, key=lambda u: (u["name"], u["duration_ms"]))

#Sort by status (fail before pass) Then by name
sort_status_name = sorted(test_results, key=lambda u: (u["status"] == "pass", u["name"]))

print("\nTest Results (ascending)")
print("-" * 50)

for test in sort_ascending:
    print(
        f"{test['name']}"
        f"{test['module']:<12}"
        f"{test['duration_ms']:>8}ms   "
        f"{test['status']:<6}   "
        
    )

print("\nSorted by: Modulename/Duration")
print("-" * 50)

for test in sort_module_duration:
    print(
        f"{test['name']}"
        f"{test['module']:<12}"
        f"{test['duration_ms']:>8}ms   "
        f"{test['status']:<6}   "
    )

print("\nSorted by: Fail/Pass and name:")
print("-" * 50)

for test in sort_status_name:
    print(
        f"{test['name']}"
        f"{test['module']:<12}"
        f"{test['duration_ms']:>8}ms   "
        f"{test['status']:<6}   "
   )

#------Map and Filter------
#use map to just extract the test names
test_names = list(map(lambda x: x["name"], test_results)) #use list() to get the result
test_failures = list(map(lambda x: x["name"],
                        filter(lambda x: x["status"] == "fail",test_results)
                        )
                )
slow_tests = list(map(lambda x: x["name"],
                        filter(lambda x: x["duration_ms"] > 1500 ,test_results)
                        )
                )

summaries = list(
    map(
        lambda x: f"✅ {x['name']} ({x['duration_ms']}ms)"
        if x["status"] == "pass"
        else f"❌ {x['name']} ({x['duration_ms']}ms)",
        test_results
    )
)


modules = map(lambda x: x["module"], test_results)
unique_modules = set(modules)

print("\nMapped test names:")
print(test_names)

print("\nMapped test failures:")
print(test_failures)

print("\nTests slower than 1500ms:")
print(slow_tests)

print("\nSummaries List:")
print(summaries)

print("\nUnique Modules:")
print(unique_modules)


#------Reduce------
total_duration = reduce(lambda acc, r: acc + r["duration_ms"], test_results, 0)
total_failure_time = reduce(lambda acc, r: acc + r["duration_ms"], 
                             filter(lambda x: x["status"] == "fail", test_results), 0)
longest_test_name= reduce(lambda acc, r: acc if len(acc) > len(r["name"]) else r["name"], test_results)
module_summary = reduce(lambda acc, r: ( acc.update({r["module"]: acc.get(r["module"], 0) + 1}) or acc),
    test_results,
    {}
)

print(f"\nTotal Duration: {total_duration}ms")
print(f"\nTotal Failure Time: {total_failure_time}ms")
print(f"\nLongest Name (By Character Count): {longest_test_name}")
print(f"\nComplete Module Summary: {module_summary}")


#------Zip------
endpoints = ["/login", "/search", "/checkout", "/profile"]
expected_codes = [200, 200, 201, 200]
actual_codes = [200, 500, 201, 403]


print("\nCompare Expected vs. Actual")
for endpoints, expected_codes, actual_codes in zip(endpoints, expected_codes, actual_codes):
    status = "✅Pass" if expected_codes == actual_codes else "❌Fail"
    print(f"{status}, {endpoints}, {expected_codes}, {actual_codes}")


rows = [
    (t["name"], t["module"], t["duration_ms"], t["status"])
    for t in test_results
]

test_names, test_modules, test_durations, test_statuses = zip(*rows)

print(f"\nTest Names: {test_names}")
print(f"Test Modules: {test_modules}")
print(f"Test Names: {test_durations}")
print(f"Test Names: {test_statuses}")

test_name_duration_dict = dict(zip(test_names,test_durations))

print(f"\nTest Names and Durations: {test_name_duration_dict}")