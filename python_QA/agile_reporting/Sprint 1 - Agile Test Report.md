# Sprint 1 - Agile Test Report

**Project:** Architect Hours QA  
**Sprint:** 1  
**Date:** 14 September 2025  
**Tester:** Yulver Musa

---

## 1. Summary
- **Total Test Cases:** 30  
- **Executed:** 30  
- **Passed:** 28  
- **Failed:** 2  
- **Blocked:** 0  

---

## 2. Test Case Execution

| Title                     | Test Case ID | Input Type    | Test Input           | Expected Result | Notes                                 | Test Result | Bug/Issue Link |
|----------------------------|--------------|---------------|--------------------|----------------|--------------------------------------|------------|----------------|
| Successful Test Case #1    | AH-01        | Name          | John               | Success        | Simple first name                     | Passed     | -              |
| Successful Test Case #2    | AH-02        | Name          | John               | Success        | Trailing space should be ignored      | Passed     | -              |
| Successful Test Case #3    | AH-03        | Name          | John Anderson      | Success        | First and last name                   | Passed     | -              |
| Successful Test Case #4    | AH-04        | Name          | John Anderson      | Success        | Trailing space should be ignored      | Passed     | -              |
| Successful Test Case #5    | AH-05        | Name          | John Anderson      | Success        | Leading space should be ignored       | Passed     | -              |
| Successful Test Case #6    | AH-06        | Name          | John   Anderson    | Success        | Multiple spaces inside the name       | Passed     | -              |
| Successful Test Case #7    | AH-07        | Name          | Anne-Marie Muller  | Success        | First and last name with hyphen       | Failed     | [BUG-001](https://github.com/yulver-musa/QA_Portfolio/issues/2) |
| Successful Test Case #8    | AH-08        | Name          | Henry O'Brian      | Success        | First and last name with apostrophe   | Failed     | [BUG-002](https://github.com/yulver-musa/QA_Portfolio/issues/3) |
| Successful Test Case #9    | AH-09        | Name          | Димитър Иванов     | Success        | First and last name in Cyrillic       | Passed     | -              |
| Successful Test Case #10   | AH-10        | Project Count | 0                  | Success        | Zero is valid                          | Passed     | -              |
| Successful Test Case #11   | AH-11        | Project Count | 5                  | Success        | Valid integer                          | Passed     | -              |
| Successful Test Case #12   | AH-12        | Project Count | 13                 | Success        | Valid integer                          | Passed     | -              |
| Successful Test Case #13   | AH-13        | Project Count | 21                 | Success        | Valid integer                          | Passed     | -              |
| Successful Test Case #14   | AH-14        | Project Count | 125                | Success        | Valid integer                          | Passed     | -              |
| Successful Test Case #15   | AH-15        | Project Count | -0                 | Success        | Should treat as zero                    | Passed     | -              |
| Unsuccessful Test Case #1  | AH-16        | Name          | " "                | Unsuccessful   | Only spaces                             | Passed     | -              |
| Unsuccessful Test Case #2  | AH-17        | Name          | ""                 | Unsuccessful   | Blank input                             | Passed     | -              |
| Unsuccessful Test Case #3  | AH-18        | Name          | John123            | Unsuccessful   | Numbers in name                          | Passed     | -              |
| Unsuccessful Test Case #4  | AH-19        | Name          | 1234               | Unsuccessful   | Only numbers                             | Passed     | -              |
| Unsuccessful Test Case #5  | AH-20        | Name          | Jo$n1234           | Unsuccessful   | Special Characters and numbers           | Passed     | -              |
| Unsuccessful Test Case #6  | AH-21        | Name          | John @Dollar       | Unsuccessful   | Special character @                     | Passed     | -              |
| Unsuccessful Test Case #7  | AH-22        | Name          | John.dollar@test.io| Unsuccessful   | Email instead of name                     | Passed     | -              |
| Unsuccessful Test Case #8  | AH-23        | Project Count | 6.5                | Unsuccessful   | Float is invalid                          | Passed     | -              |
| Unsuccessful Test Case #9  | AH-24        | Project Count | 0.34               | Unsuccessful   | Float is invalid                          | Passed     | -              |
| Unsuccessful Test Case #10 | AH-25        | Project Count | 3.14               | Unsuccessful   | Float is invalid                          | Passed     | -              |
| Unsuccessful Test Case #11 | AH-26        | Project Count | 10.0               | Unsuccessful   | Float is invalid                          | Passed     | -              |
| Unsuccessful Test Case #12 | AH-27        | Project Count | ""                 | Unsuccessful   | Blank input                               | Passed     | -              |
| Unsuccessful Test Case #13 | AH-28        | Project Count | -9                 | Unsuccessful   | Negative number                           | Passed     | -              |
| Unsuccessful Test Case #14 | AH-29        | Project Count | -10.00             | Unsuccessful   | Negative number                           | Passed     | -              |
| Unsuccessful Test Case #15 | AH-30        | Project Count | abc                | Unsuccessful   | Non-numeric input                          | Passed     | -              |

---

## 3. Defect Summary
- **Total Defects Raised:** 2  
- **Severity:** 2 High,  
- **Status:** Open  
- **Linked Issues:**  
  - [BUG-001: Hyphen](https://github.com/yulver-musa/QA_Portfolio/issues/2)  
  - [BUG-002: Apostrophe](https://github.com/yulver-musa/QA_Portfolio/issues/3)

---

## 4. Notes / Recommendations
- Regression testing may be needed for inputs with **special characters and hyphens/apostrophes** (AH-07, AH-08).  
- Consider updating input validation in the code for names with hyphens or apostrophes.  
- Next sprint: Automate all 30 test cases using PyTest and link each failure to GitHub issues.   

---

**End of Report**

