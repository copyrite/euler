;;;; If we list all the natural numbers below 10 that are multiples of
;;;; 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
;;;; 
;;;; Find the sum of all the multiples of 3 or 5 below 1000.

(defun arithmetic-sum (n)
  "Sum of integers 1, ..., n."
  (/ (* n (+ n 1)) 2)
)

(defun arithmetic-sum-multiples (n m)
  "Sum of multiples of m up to n."
  (* m (arithmetic-sum (floor n m)))
)

(defun sum-of-multiples-of-3-or-5 (n)
  "Sum of multiples of 3 or 5 up to n."
  (+
    (arithmetic-sum-multiples n 3)
    (arithmetic-sum-multiples n 5)
    (- (arithmetic-sum-multiples n 15))
  )
)

(princ (sum-of-multiples-of-3-or-5 (- 1000 1)))
