class TestCase:
    """Represents a single test case.

    Class Attributes:
        total_created (int): Count of all TestCase objects ever created

    Instance Attributes:
        name (str): Test name (e.g., "test_login_valid")
        description (str): What this test verifies
        priority (str): "high", "medium", or "low" (default: "medium")
        tags (list): Labels like ["smoke", "regression"]
    """
    # TODO: Implement __init__, run(), and a class method
    total_created = 0

    def __init__(self, name, description, priority="medium", tags=None):
        self.name = name
        self.description = description
        self.priority = priority

        if tags is None:
            self.tags = []
        else:
            self.tags = tags

        TestCase.total_created += 1 
    

    def run(self):
       return "fail" not in self.name
        
        
    @classmethod
    def from_dict(cls, data):
        """Create a TestCase from a dictionary.
        Example: TestCase.from_dict({"name": "test_login", "priority": "high"})
        """
        return cls(
            data["name"],
            data["description"],
            data.get("priority", "medium"),
            data.get("tags", [])
        )
    
    @staticmethod
    def is_valid_name(name):
        """Check if name starts with 'test_' and has no spaces."""
  
        if not name.startswith("test_"):
            return False

        for char in name:
            if char == " ":
                return False

        return True
    
class TestResult:
    """The outcome of running a single test.

    Instance Attributes:
        test_name (str): Which test was run
        status (str): "pass" or "fail"
        duration_ms (float): How long it took
        error_message (str or None): Error details if failed
    """
    def __init__(self, test_name, status, duration_ms, error_message):
        self.test_name = test_name
        self.status = status
        self.duration_ms = duration_ms
        self.error_message = error_message
        
        
    

    def summary(self):
        """Return a one-line summary like: '✅ test_login (120ms)'"""
        if self.status == "pass":
            return f"✅ {self.test_name} ({self.duration_ms}ms)"
        else:
            return f"❌ {self.test_name} ({self.duration_ms}ms)"

class TestSuite:
    """A collection of test cases.

    Instance Attributes:
        name (str): Suite name
        tests (list): List of TestCase objects

    Methods:
        add_test(test): Add a TestCase
        remove_test(name): Remove by name
        get_by_priority(priority): Return tests matching the priority
        count(): Return number of tests
    """
    def __init__(self, name, tests=None):
        self.name = name
        if tests is None:
            self.tests = []
        else:
            self.tests = tests
    
    def add_test(self,test):
        self.tests.append(test)
    
    def remove_test(self,name):
        for test in self.tests:
            if test.name == name:
                self.tests.remove(test)
                break
            
    def get_by_priority(self,priority):
        matching_tests = []
        for test in self.tests:
            if test.priority == priority:
                matching_tests.append(test)
        
        return matching_tests
            
    
    def count(self):
        return len(self.tests)
    

class TestRunner:
    """Executes a TestSuite and collects results.

    Methods:
        run(suite): Run all tests in a suite, return list of TestResult
        summary(results): Print a formatted summary
    """
    # TODO: Implement

    def run(self, suite):
        """Run each test in the suite and return a list of TestResults."""
        import time
        import random
        results = []
        for test in suite.tests:
            start = time.time()
            passed = test.run()
            duration = (time.time() - start) * 1000
            # Simulate varying duration
            duration += random.uniform(50, 500)
            result = TestResult(
                test.name,
                "pass" if passed else "fail",
                round(duration, 1),
                None if passed else f"{test.name} assertion failed"
            )
            results.append(result)
        return results 
    
    def summary(self, results):
        for result in results:
            print(result.summary()) 
        
        passed = 0
        failed = 0
        
        for result in results:
            if result.status == "pass":
                passed += 1
            else:
                failed += 1
        
        print(f"\nPassed: {passed}")
        print(f"\nFailed: {failed}")

def main():
    test1 = TestCase( #Passing Test
    "test_login_valid",
    "Verify valid login works",
    "high",
    ["smoke", "login"]
    )

    test2 = TestCase( #Failing Test
    "test_login_fail",
    "Verify invalid login handling",
    "high",
    ["regression", "login"]
    )

    test3 = TestCase.from_dict({ #Passing Test
    "name": "test_integration",
    "description": "Test APIs can talk to front end",
    "priority": "medium",
    "tags": ["integration", "api"]
    })

    test4 = TestCase( #Passing Test
    "test_db_access",
    "Verify access to database"
    )

    test5 = TestCase.from_dict({ #Failing Test
    "name": "test_integration_fail",
    "description": "Verify failed connectivity",
    "priority": "high",
    "tags": ["integration", "api"]
    })

    test6 = TestCase( #Failing Test
    "test_password_reset_fail",
    "Verify failed password reset",
    "low",
    ["password"]
    )
    
    test_suite = TestSuite("test_suite", [test1, test2, test3, test4, test5, test6])
    
    high_priority = test_suite.get_by_priority("high")
    
    print("═" * 40)
    print(" High Priority Tests")
    print("═" * 40)
    
    for tests in high_priority:
        print(tests.name)
    
    test_runner = TestRunner()
    results = test_runner.run(test_suite)
    
    print("═" * 40)
    print(" Test Results Summary ")
    print("═" * 40)
    
    test_runner.summary(results)

if __name__ == "__main__":
    main()
    
    
    