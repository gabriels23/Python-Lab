"use strict";

function innerProduct(input) {
    // main :: IO ()
    var main = function main(xs) {
        return sum(flatten(xs));
    };

    // GENERIC -----------------------------------------------------------------
    // JS - Prelude

    // flatten :: NestedList a -> [a]
    var flatten = function flatten(t) {
        return Array.isArray(t) ? [].concat.apply([], t.map(flatten)) : t;
    };

    // sum :: [Num] -> Num
    var sum = function sum(xs) {
        return xs.reduce(function (a, x) {
            return a + x;
        }, 0);
    };

    // JXA MAIN ----------------------------------------------------------------
    return main(input);
}
