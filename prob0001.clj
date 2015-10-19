(defn multiple-of-3-or-5? [n]
  (or (= 0 (mod n 3))
      (= 0 (mod n 5))))

(reduce + (filter multiple-of-3-or-5? (range 1000)))
