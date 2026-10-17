# SauceDemo Test Plan

## 1. Objective
This test plan defines the validation scope for the SauceDemo login and shopping flow available at https://www.saucedemo.com/.

The primary goal is to verify that users can successfully log in, browse products, add and remove items, complete checkout, and log out without critical issues.

## 2. Scope
### In Scope
- Login page rendering and validation
- Valid/invalid user authentication
- Product listing and sorting
- Add/remove from cart
- Cart review and checkout flow
- Order completion confirmation
- Logout behavior
- Browser compatibility with Chromium-based execution

### Out of Scope
- API testing
- Performance benchmarking
- Security penetration testing
- Third-party integrations beyond the demo app

## 3. Test Approach
The project will use a Playwright-based automated test strategy with a page-object model. Test execution will focus on happy-path flows and essential negative scenarios that validate business-critical functionality.

## 4. Test Environment
- Application URL: https://www.saucedemo.com/
- Browser: Chromium (Playwright)
- Execution mode: Headless for CI-friendly automation
- Test framework: pytest + Playwright

## 5. Test Data
### Valid Users
- standard_user / secret_sauce
- problem_user / secret_sauce
- performance_glitch_user / secret_sauce

### Invalid Credentials
- wrong username / wrong password
- locked_out_user / secret_sauce

## 6. Entry Criteria
- Application is reachable at the production demo URL
- Browser automation dependencies are installed and working
- Test environment has stable internet access
- Required browser binaries are available

## 7. Exit Criteria
- All planned smoke and regression tests pass
- No critical or high-priority defects remain open
- Checkout flow has been verified with a valid end-to-end scenario
- Test results are documented and stored in the project run output

## 8. Risks and Assumptions
### Risks
- Login page text may change over time
- Product inventory/order counts may vary
- Browser rendering differences may affect UI timing

### Assumptions
- The app is a demo environment intended for test automation
- The username/password combinations are stable for the validation window
- Browser automation is allowed on the target site

## 9. Test Cases

### A. Smoke Tests
1. Open login page
2. Validate page elements are visible
3. Login with valid standard user
4. Verify inventory page loads
5. Add one item to cart
6. Check cart count updates
7. Complete checkout with valid data
8. Verify order completion message

### B. Functional Tests
#### Login
- TC-01: User can log in with valid credentials
- TC-02: User cannot log in with invalid credentials
- TC-03: Locked-out user is rejected
- TC-04: Username field is required
- TC-05: Password field is required

#### Product Listing
- TC-06: Products are displayed on inventory page
- TC-07: Product names and prices are visible
- TC-08: Add to cart button works for a selected product
- TC-09: Remove from cart updates state correctly

#### Cart and Checkout
- TC-10: Cart displays correct item count and price summary
- TC-11: User can continue from cart to checkout
- TC-12: User can enter valid checkout information
- TC-13: Purchase is completed successfully
- TC-14: Validation prevents missing checkout fields

#### Logout
- TC-15: User can log out and return to login page

## 10. Test Execution Order
1. Login validation
2. Product page checks
3. Cart actions
4. Checkout validation
5. Logout verification
6. Regression re-run

## 11. Acceptance Criteria
The feature is considered ready when:
- all smoke tests pass,
- core happy paths are validated,
- negative login and checkout validations are covered,
- no critical functional issues remain unresolved.

## 12. Deliverables
- Automated Playwright test scripts
- Test execution output and results
- Defect log for any failing scenarios
- Summary report for sign-off
