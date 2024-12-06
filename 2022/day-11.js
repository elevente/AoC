const input = `Monkey 0:
  Starting items: 99, 63, 76, 93, 54, 73
  Operation: new = old * 11
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 1:
  Starting items: 91, 60, 97, 54
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 3
    If false: throw to monkey 2

Monkey 2:
  Starting items: 65
  Operation: new = old + 7
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 5

Monkey 3:
  Starting items: 84, 55
  Operation: new = old + 3
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 4:
  Starting items: 86, 63, 79, 54, 83
  Operation: new = old * old
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 0

Monkey 5:
  Starting items: 96, 67, 56, 95, 64, 69, 96
  Operation: new = old + 4
  Test: divisible by 5
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 6:
  Starting items: 66, 94, 70, 93, 72, 67, 88, 51
  Operation: new = old * 5
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 5

Monkey 7:
  Starting items: 59, 59, 74
  Operation: new = old + 8
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 3`;
	const monkeys = [{
		items: [99, 63, 76, 93, 54, 73],
		operation: "old * 11",
		test: {
			division: 2,
			true: 7,
			false: 1
		},
		inspected: 0
	}, {
		items: [91, 60, 97, 54],
		operation: "old + 1",
		test: {
			division: 17,
			true: 3,
			false: 2
		},
		inspected: 0
	}, {
		items: [65],
		operation: "old + 7",
		test: {
			division: 7,
			true: 6,
			false: 5
		},
		inspected: 0
	}, {
		items: [84, 55],
		operation: "old + 3",
		test: {
			division: 11,
			true: 2,
			false: 6
		},
		inspected: 0
	}, {
		items: [86, 63, 79, 54, 83],
		operation: "old * old",
		test: {
			division: 19,
			true: 7,
			false: 0
		},
		inspected: 0
	}, {
		items: [96, 67, 56, 95, 64, 69, 96],
		operation: "old + 4",
		test: {
			division: 5,
			true: 4,
			false: 0
		},
		inspected: 0
	}, {
		items: [66, 94, 70, 93, 72, 67, 88, 51],
		operation: "old * 5",
		test: {
			division: 13,
			true: 4,
			false: 5
		},
		inspected: 0
	}, {
		items: [59, 59, 74],
		operation: "old + 8",
		test: {
			division: 3,
			true: 1,
			false: 3
		},
		inspected: 0
	}];
	const MODULO = 9699690;

	// for (let round = 0; round < 20; round++) {
	for (let round = 0; round < 10000; round++) {
		for (let monkey = 0; monkey < monkeys.length; monkey++) {
			const currentMonkey = monkeys[monkey];
			// for (let item = 0; item < currentMonkey.items.length; item) {
			while (currentMonkey.items.length > 0) {
				let currentItem = currentMonkey.items[0];
				currentMonkey.inspected++;
				const old = currentItem;
				currentItem = eval(currentMonkey.operation);
				if (currentItem > MODULO) {
					currentItem = currentItem % MODULO;
				}
				// currentItem = Math.floor(currentItem / 3);
				if (currentItem % currentMonkey.test.division == 0) {
					monkeys[currentMonkey.test.true].items.push(currentItem);
				} else {
					monkeys[currentMonkey.test.false].items.push(currentItem);
				}
				currentMonkey.items.splice(0, 1);
			}
		}
		console.log(monkeys[0].inspected);
	}

	monkeys.sort((a, b) => a.inspected - b.inspected).reverse();
	const monkeyBusiness = monkeys[0].inspected * monkeys[1].inspected;
	// document.body.innerHTML = monkeyBusiness;
	console.log(monkeyBusiness);