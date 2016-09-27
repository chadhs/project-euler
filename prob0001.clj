(defn multiple-of-3-or-5? [n]
  (or (= 0 (mod n 3))
      (= 0 (mod n 5))))

(reduce + (filter multiple-of-3-or-5? (range 1000)))

;; let's do the traditional FizzBuzz exercise for fun too!
(defn fizzbuzz
  "prints FizzBuzz results for a range of 1-num"
  [num]
  (let [nums (range 1 (inc num))]
    (map
     #(cond
        (zero? (mod % 15)) (print-str "FizzBuzz")
        (zero? (mod % 5))  (print-str "Buzz")
        (zero? (mod % 3))  (print-str "Fizz")
        :else              (print-str %))
     nums)))

(fizzbuzz 100)
