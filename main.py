total_working_days = []
library_order = []
def optimize(libraries, total_days , skip_library=None):
    library_order.append(skip_library)
    total_days_to_signup = 0
    libraries_performance = {}
    if (len(libraries) == 0):
        return

    for library in libraries:
        number_of_books = library.numBooks
        days_to_signup = library.signUpTime
        scan_limit = library.scanningLimit
        libraries_performance[library.id]=(working_days(number_of_books, scan_limit, days_to_signup))

    library_id = min(libraries_performance, key=libraries_performance.get)
    total_days_to_signup += libraries[library_id].days_to_signup
    return optimize(libraries, total_days, library_id)

def working_days(number_of_books, scan_limit, days_to_signup):
    return number_of_books/scan_limit + days_to_signup