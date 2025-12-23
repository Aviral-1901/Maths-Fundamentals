# Vectors - Python Programs

Vectors are quantities with magnitude and direction.
This folder contains Python programs for vector operations and manipulation.

01_manual_normalization.py
-> In this file we created a Python list and passed it into a normalize function.
-> In normalize function we converted that list to numpy arrays so that lists, tuples or numpy
    array itself gets converted to numpy arrays for easier calculation
-> Then the components of vectors were squared using v * np.conj(v) which is essential for complex 
   numbers.
-> We added the squared components and used np.real() because we squared using np.con() which gives 
   complex number and we only need real number as magnitude and the final magnitude was calculated using np.sqrt() as magnitude = squareRoot(x^2 + y^2 + z^2)
-> np.linalg.norm(vector) is the numpy method to calculate magnitude easily


# Day 2 dot product
- key learning : dot product is mainly used for finding similarity between two vectors
                 High positive value : Same direction
                 Zero : Orthogonal (perpendicular)
                 High negative value: Different direction
-  Note: Dot product measures alignment AND magnitude.
-  Code: For 1D real-valued vectors of the same length, all of the following compute the dot      product:
        np.dot(v1,v2) 
        v1 @ v2
        np.sum(v1 * v2)  