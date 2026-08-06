"""
=============================
   DIAMOND PROBLEM IN PYTHON
=============================

Definition:
-----------
    The Diamond Problem occurs in Multiple Inheritance when two parent
    classes inherit from the same base class and a child class inherits
    from both parents.

Structure:
            -----------

                 A
                / \
               B   C
                \ /
                 D

Example:
    --------

    class A:
        def show(self):
            print("Class A")

    class B(A):
        def show(self):
            print("Class B")

    class C(A):
        def show(self):
            print("Class C")

    class D(B, C):
        pass

    obj = D()
    obj.show()

Output:
-------
    Class B

Reason:
-------
    Python follows Method Resolution Order (MRO), so it searches in this order:

    D → B → C → A → object

    Since B comes before C, B.show() is executed.

Check MRO:
----------
    print(D.mro())

Summary:
--------
    • Occurs in Multiple Inheritance.
    • Solved using Method Resolution Order (MRO).
    • Python uses the C3 Linearization Algorithm to avoid ambiguity.
"""