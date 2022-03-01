const countConstruct = (target, wordBank) => {
    if (target === '') return 1;

    let totalCount = 0;

    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const numWaysForRest = countConstruct(target.slice(word.lengh), wordBank);
            totalCount += numWaysForRest;
        }
    }

    return totalCount;
};

console.log(countConstruct('purple', ['purple']));