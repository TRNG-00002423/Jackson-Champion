#Test results for 5 tests
test1_name = "test_login"
test1_duration = 1200
test1_status = "✅ PASS"

test2_name = "test_search"
test2_duration = 850
test2_status = "✅ PASS"

test3_name = "test_checkout"
test3_duration = 2300
test3_status = "❌ FAIL"

test4_name = "test_profile"
test4_duration = 450
test4_status = "✅ PASS"

test5_name = "test_logout"
test5_duration = 180
test5_status = "✅ PASS"

total_duration = test1_duration + test2_duration + test3_duration + test4_duration + test5_duration

#Table Structure
print("┌──────────────────┬──────────────┬──────────┐")
print(f"│ {'Test Name':<16} │ {'Duration':>10} ms│ {'Status':<8} |")
print("├──────────────────┼──────────────┼──────────┤")

print(f"│ {test1_name:<16} │ {test1_duration:>10,} ms│ {test1_status:<8}│")
print(f"│ {test2_name:<16} │ {test2_duration:>10,} ms│ {test2_status:<8}│")
print(f"│ {test3_name:<16} │ {test3_duration:>10,} ms│ {test3_status:<8}│")
print(f"│ {test4_name:<16} │ {test4_duration:>10,} ms│ {test4_status:<8}│")
print(f"│ {test5_name:<16} │ {test5_duration:>10,} ms│ {test5_status:<8}│")

print("├──────────────────┼──────────────┼──────────┤")
print(f"│ {'TOTAL':<16} │ {total_duration:>10,} ms│ {'4/5 Pass':<8} │")
print("└──────────────────┴──────────────┴──────────┘")