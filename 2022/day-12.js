const input = `abcccccccccccaaaaacccccccaaaaaaccccccccccccccccccccccccccccccccaaaaaaaaaaaaaacccccccccccccccccccaaaaaacccccccacccccccccaaccaaccccccccccccccccccccccccccccccaaaaaa
abcccccccccccaaaaaaacccccaaaaaaccccccccaaccccccccccaaaaccccccccaaaaaaaaaaaaaccccccccccccccccccccaaaaaaccccaaaacccccccccaaaaaaccccccccccccccccccccccccccccccccaaaa
abccccccccccaaaaaaaacccccaaaaaccccccccaaaacccccccccaaaacccccccccccaaaaaaacccccccccccccccccccccccaaaaacccccaaaaaaccccccccaaaaacccccccccccaaaccccccccccccccccccaaaa
abccccccccccaaaaaaaaccccccaaaaacccccccaaaacccccccccaaaacccccaaaccccaaaaaaccccccccccccccccccccccccaaaaacccccaaaaacccccccaaaaaacccccccccccaaaacccccccccccccccccaaaa
abccccccccccaaaaaaccccccccaaaaacccccccaaaaccccccccccaaacccccaaaaccaaaaaaaacccccccccccccccccccccccaaaaaccccaaaaacccccccaaaaaaaaccccccccccaaaaccaaccccccccccccaaaaa
abcccccccccccccaaaccccccccccccccccccccccccccccccccccccccccccaaaaccaaaaaaaaccccccccccccccccccccccccccccccccaccaaccccaaaaaaaaaaacccccccccccaaaaaaccccccccccccccaccc
abcacccccccccccccaaaccccccccccccccaaacccccccccccccccccccccccaaaccaaaacccaaacccccccccccccccccccccccaacccccccccccccccaaacccaaccccccccccccccaaaalllllccccccccccccccc
abaacccccccccccccaaaaaacccccccccccaaaccccccccccccccccccccccccccccaaaccccaaaccccccccccccccccccccccaaccccccccccccccccaaaaaaaaccccccccccccccckklllllllccccaaaccccccc
abaaaaacccccccccaaaaaaacccccccccaaaaaaaacccccaacccccccccccccccccccccccccaaaccccccccaacccccccccaaaaacaacaacaacccccaaaaaaaaccccccccccccaaakkkkllllllllcccaaaccccccc
abaaaaaccccccccaaaaaaaacccccccccaaaaaaaacccccaaaaaacccccccccccccccccccccaaaccccccaaaacacccccccaaaaaaaacaaaaaccccaaaaaaaaaccccccccckkkkkkkkkklsssslllcccaaaaaacccc
abaaaccccccccccaaaaaaacccccccccccaaaaacccccccaaaaaaccccccccccccccccccaaaaaaaaccccaaaaaacccccccccaaaaacaaaaacccccaaaaaaaacccaaaccjjkkkkkkkkkssssssslllcccaaaaacccc
abaaaccccccccccccaaaaaacccccaacccaaaaaaccccaaaaaaaccaaaccccccccccccccaaaaaaaacccccaaaacccccccccaaaaaccaaaaaacccccccaaaaaaccaaaajjjjkkkkkkssssssssslllcddaaaaccccc
abcaaacccccccccccaaaaaacaaacaacccaaaaaaccccaaaaaaaaaaaaaaccccccccccccccaaaaaccccccaaaaccccaaaaaaacaaacccaaaaaaacccaaaaaaaccaaajjjjrrrrrrssssuuuussqmmddddaaaccccc
abccaacccccccccccaaccccccaaaaacccaaaccaccccaaaaaaaaaaaaaacccccccccccccaaaaaacccccaacaaccccaaaaacccaaccccacccaaaaaaaaaccaaccaaajjjrrrrrrrrssuuuuuvqqmmmdddaaaccccc
abccccccccaaccccccccccccccaaaaaacccccccccccccaaaaaaaaaaaccccccccccccccaaaaaacccccccccccccaaaaaaccccccccccccaaaaaaaaaacccccccccjjjrrruuuuuuuuuuuvvqqmmmmddddaccccc
abaacccccaaaaccccccccccccaaaaaaacccccccccccccaacccccaaaaacccccccccccccaccaaacccccccccccccaaaaaacccccccccccaaaaaaaaccccccccccccjjjrrruuuuuuuuxyyvvqqqmmmddddcccccc
abaacccccaaaacccccccccccaaaaaaccccccccaaccccccccacccaaaaacccccccccccccccccccccccccccccccccaaaaacccccccccccaaaaaaacccccccccccccjjjrrttuxxxxuxxyyvvqqqqmmmmddddcccc
abaacccccaaaacccccccccccaacaaacccccaaaaacccaaaaaaaccccccccccccccccccccccccccccccccccccccccaaacccccccccccccccaaaaaaccccccccccccjjjrrtttxxxxxxyyyvvqqqqqmmmmdddcccc
abacccccccccccccccccccccccccaaccccccaaaaaccaaaaaaaccccccccaaccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccccccjjjqrrttxxxxxxyyyvvvvqqqqmmmdddcccc
abccccccccccccccccccccccccccccccccccaaaaaccaaaaaaacccccccaaaccccccccccaaaccccccccccccccccccaaaccccccccccccccaaccccccccccaaccccjjjqqqtttxxxxxyyyyyvvvqqqqmmmeeeccc
SbaaccccccaccaaacccccccccccccccccccaaaaacccaaaaaaaaccccaaaaaaaacccccccaaacaaccccccccccccccaaaaaaccccccccccccccccccccccaaaaaaccciiiqqqttxxxxEzyyyyyvvvqqqnnneeeccc
abaaccccccaaaaaaccccccccccccccccccccccaaccaaaaaaaaaacccaaaaaaaacccccaaaaaaaaccccccccccccccaaaaaaccccccccccccccccccccccaaaaaaccciiiqqtttxxxyyyyyyyvvvvqqqnnneeeccc
abaaaaacccaaaaaaccccccccccccccccccccccccccaaaaaaaaaaccccaaaaaaccccccaaaaaaaaccccccccccccccaaaaaacccccccccccccccccccccccaaaaacciiiqqqttxxyyyyyyywvvvvrrrqnnneeeccc
abaaaaacccaaaaaaaccccccccaaaccccccccccccccaacaaaccccccccaaaaaaccccccaaaaaaaccccccccccccccccaaaaaccccccccccccccccccccccaaaaaccciiiqqtttxxxyyyyywwwvrrrrrnnneeecccc
abaaaccccaaaaaaaaccccccccaaaacccccccccccccccccaaccccccccaaaaaaccccccccaaaaaccccccccccccccccaacaaccccccccccccccccccccccaaaaaccciiqqqttxxxwwwwyyywwrrrrnnnnneeecccc
abaaaccccaaaaaaaaccccccccaaaacccccaaaaacccccccaaccccccccaaccaacccccccaaacaaacccccccccccccccccccccccccccccccccccccccccccccccccciiqqqtttwwwwwwywwwrrrrnnnnneeeccccc
abcaaaccccccaaaccccccccccaaaccccccaaaaacccccccccccccaaaaccccccccccccccaacccccccccccccccccccccccccccccccaaaacccccccccccccccccciiiqqqtttssssswwwwwrrrnnnneeeecccccc
abccaaccccccaaaccccccccccccccccccaaaaaacccccccccccccaaaaccccccccccccccccccccccccccccccccccccccccccccccaaaaacccccccccccccccccciiiqqqqtssssssswwwwrronnnfeeeacccccc
abcccccccccccccccccccccccccccccccaaaaaacccccccccccccaaaaccccccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccccccccccciiiiqqppssssssswwwwrroonfffeaacccccc
abcccccccccccccccccccccccccccccccaaaaaacaaaccccccccccaacccccccccccccccccccccccccccccccccaaacccccccccccaaaaaaccccccccccccccccccihhpppppppppsssssrrroonfffaaaaacccc
abcccccccccccccccccccccccccccccccccaacccaaaaacccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccaaaaaccccccccccccccccccchhhhppppppppppssssrooofffaaaaaacccc
abccccccccaaaccccccccccccccccccccccccccaaaaacccccccccccccccccccccccccccccccccccccaccccaaaaaaaaccccccccccaaacccccccccccccccccccchhhhhhhhhpppposssoooofffaaaaaccccc
abccccccccaaaacccccaaccccccccccccccccccaaaaaccccccccccccccccccccccccaaccccccccccaaccccaaaaaaaacccccccccccccccccccccccccccccccccchhhhhhhhhgppooooooofffaaaaacccccc
abaaccccccaaaacccccaacaaccccccccccccccccaaaaacccccccccccccccaacaaccaaaaaaccccaaaaacaacaaaaaaacccccccccccccccccccccccccccccccccccccchhhhhhgggooooooffffaaaaaaccccc
abaaacccccaaaacccccaaaaaccccccccccccccccaaccccccccccccccccccaaaaaccaaaaaaccccaaaaaaaacccaaaaaccccccccccccccccccccccccaaacaacccccccccccccgggggooooffffccccaacccccc
abaaaccccccccccccaaaaaaccccaaccccccccccccccccccaaacccccccccccaaaaaaaaaaaacaacccaaaaaccccaacaaacccccccccccccccccccccccaaaaaaccccccccccccccaggggggggfffcccccccccccc
abaaaccccccccccccaaaaaaaacaaaaccccccccaaaccccccaaaacccccccccaaaaaaaaaaaaaaaaccaaaaacccccaaaaaccccccccccccccaaccccccccaaaaaaccccccccccccccaagggggggfccccccccccccca
abaacccccccccccccaccaaaaacaaaaccccccccaaaccccccaaaacccccccccaaaaccaaaaaaaaaaccaacaaaccccccaaaccccccccccccaaaaaacccccaaaaaaacccccccccccccaaaaccggggcccccccccccccaa
abaacccccccccccccccaaacaccaaaacccccaaaaaaaaccccaaaccccccccccccaaccaaaaaaaacccccccaacccccaacaaaaacccccccccaaaaaacccccaaaaaaaaccccccccccccaaaccccccccccccccccaaacaa
abcccccccccccccccccaaccccccccccccccaaaaaaaaccccccccccccccccccccaaaaaaaaaaaccccccccccccccaaaaaaaacccccccccaaaaaacccccaaaaaaaaccccccccccccacaccccccccccccccccaaaaaa
abccccccccccccccccccccccccccccccccccaaaaaacccccccccccccccccccccaaaaaaaaaaaaccccccccccccccaaaaaaccccccccccaaaaaccccccccaaacccccccccccccccccccccccccccccccccccaaaaa`;
const example = `Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi`;

const matrix = input.split("\n").map(i => i.split(""));
// const startRow = matrix.findIndex(row => row.includes("S"));
// const startCol = matrix[startRow].indexOf("S");
// const visited = Array(matrix.length).fill().map(() => Array(matrix[0].length).fill(false));
// let solution = Infinity;

// function step(y, x, steps, stepCount, visited, path) {
// 	// console.log(y, x);
// 	path += `${y},${x}\n`;
// 	let currentVisited = JSON.parse(JSON.stringify(visited)); 
// 	currentVisited[y][x] = true;
// 	let currentCharCode = matrix[y][x].charCodeAt();
// 	if (currentCharCode == 83) {
// 		currentCharCode = 97;
// 	}
// 	let leftCharCode = x > 0 ? matrix[y][x - 1].charCodeAt() : undefined;
// 	if (leftCharCode == 69) {
// 		leftCharCode = 122;
// 	}
// 	let rightCharCode = x < matrix[y].length - 1 ? matrix[y][x + 1].charCodeAt() : undefined;
// 	if (rightCharCode == 69) {
// 		rightCharCode = 122;
// 	}
// 	let topCharCode = y > 0 ? matrix[y - 1][x].charCodeAt() : undefined;
// 	if (topCharCode == 69) {
// 		topCharCode = 122;
// 	}
// 	let bottomCharCode = y < matrix.length - 1 ? matrix[y + 1][x].charCodeAt() : undefined;
// 	if (bottomCharCode == 69) {
// 		bottomCharCode = 122;
// 	}
// 	if (currentCharCode == 69) {
// 		console.log(`found it: ${stepCount}`);
// 		if (solution > stepCount) {
// 			solution = stepCount;
// 		}
// 		return steps.push({ found: true, steps: stepCount, path });
// 	}
// 	if ((leftCharCode <= currentCharCode || leftCharCode == currentCharCode + 1) && !currentVisited[y][x - 1]) {
// 		// console.log("going left");
// 		steps.push([]);
// 		step(y, x - 1, steps[steps.length - 1], stepCount + 1, currentVisited, path);
// 	}
// 	if ((rightCharCode <= currentCharCode || rightCharCode == currentCharCode + 1) && !currentVisited[y][x + 1]) {
// 		// console.log("going right");
// 		steps.push([]);
// 		step(y, x + 1, steps[steps.length - 1], stepCount + 1, currentVisited, path);
// 	}
// 	if ((topCharCode <= currentCharCode || topCharCode == currentCharCode + 1) && !currentVisited[y - 1][x]) {
// 		// console.log("going up");
// 		steps.push([]);
// 		step(y - 1, x, steps[steps.length - 1], stepCount + 1, currentVisited, path);
// 	}
// 	if ((bottomCharCode <= currentCharCode || bottomCharCode == currentCharCode + 1) && !currentVisited[y + 1][x]) {
// 		// console.log("going down");
// 		steps.push([]);
// 		step(y + 1, x, steps[steps.length - 1], stepCount + 1, currentVisited, path);
// 	}
// 	// console.log(`nope: ${stepCount}`);
// 	return steps.push({ found: false, steps: stepCount });
// }

// let steps = [];
// let path = ""
// step(startRow, startCol, steps, 0, visited, path);
// console.log(solution);
// console.log(steps);

class Graph {
  constructor() {
	this.vertices = [];
	this.adjacent = {};
	// this.edges = 0;
  }

	addVertex(v) {
		this.vertices.push(v);
		this.adjacent[v] = [];
	}

	addEdge(v, w) {
		this.adjacent[v].push(w);
		// this.adjacent[w].push(v);
		// this.edges++;
	}

	bfs(goal, root = this.vertices[0]) {
		let adj = this.adjacent;

		const queue = [];
		queue.push(root);

		const discovered = [];
		discovered[root] = true;

		const edges = [];
		edges[root] = 0;

		const predecessors = [];
		predecessors[root] = null;

		const buildPath = (goal, root, predecessors) => {
			const stack = [];
			stack.push(goal);

			let u = predecessors[goal];

			while(u != root) {
				stack.push(u);
				u = predecessors[u];
			}

			stack.push(root);

			let path = stack.reverse().join('-');

			return path;
		}
	

		while(queue.length) {
			let v = queue.shift();

			if (v === goal) {
				return { 
					distance: edges[goal],
					path: buildPath(goal, root, predecessors)
				};
			}

			for (let i = 0; i < adj[v].length; i++) {
				if (!discovered[adj[v][i]]) {
					discovered[adj[v][i]] = true;
					queue.push(adj[v][i]);
					edges[adj[v][i]] = edges[v] + 1;
					predecessors[adj[v][i]] = v;
				}
			}
		}

		return false;
	}
}

const graph = new Graph();
// let start = "";
let start = [];
let end = "";

for (let y = 0; y < matrix.length; y++) {
	for (let x = 0; x < matrix[y].length; x++) {
		graph.addVertex(`${y},${x}`);
		if (matrix[y][x] == "S" || matrix[y][x] == "a") {
			start.push(`${y},${x}`);
		}
		if (matrix[y][x] == "E") {
			end = `${y},${x}`;
		}
	}
}

for (let y = 0; y < matrix.length; y++) {
	for (let x = 0; x < matrix[y].length; x++) {
		let currentCharCode = matrix[y][x].charCodeAt();
		if (matrix[y][x] == "S") {
			currentCharCode = "a".charCodeAt();
		}
		if (matrix[y][x] == "E") {
			currentCharCode = "z".charCodeAt();
		}
		if (x > 0) {
			let leftCharCode = matrix[y][x - 1].charCodeAt();
			if (matrix[y][x - 1] == "S") {
				leftCharCode = "a".charCodeAt();
			}
			if (matrix[y][x - 1] == "E") {
				leftCharCode = "z".charCodeAt();
			}
			if (leftCharCode <= currentCharCode || leftCharCode == currentCharCode + 1) {
				graph.addEdge(`${y},${x}`, `${y},${x - 1}`);
			}
		}
		if (x < matrix[y].length - 1) {
			let rightCharCode = matrix[y][x + 1].charCodeAt();
			if (matrix[y][x + 1] == "S") {
				rightCharCode = "a".charCodeAt();
			}
			if (matrix[y][x + 1] == "E") {
				rightCharCode = "z".charCodeAt();
			}
			if (rightCharCode <= currentCharCode || rightCharCode == currentCharCode + 1) {
				graph.addEdge(`${y},${x}`, `${y},${x + 1}`);
			}
		}
		if (y > 0) {
			let topCharCode = matrix[y - 1][x].charCodeAt();
			if (matrix[y - 1][x] == "S") {
				topCharCode = "a".charCodeAt();
			}
			if (matrix[y - 1][x] == "E") {
				topCharCode = "z".charCodeAt();
			}
			if (topCharCode <= currentCharCode || topCharCode == currentCharCode + 1) {
				graph.addEdge(`${y},${x}`, `${y - 1},${x}`);
			}
		}
		if (y < matrix.length - 1) {
			let bottomCharCode = matrix[y + 1][x].charCodeAt();
			if (matrix[y + 1][x] == "S") {
				bottomCharCode = "a".charCodeAt();
			}
			if (matrix[y + 1][x] == "E") {
				bottomCharCode = "z".charCodeAt();
			}
			if (bottomCharCode <= currentCharCode || bottomCharCode == currentCharCode + 1) {
				graph.addEdge(`${y},${x}`, `${y + 1},${x}`);
			}
		}
	}
}

// console.log(graph.bfs(end, start));
let min = Infinity;
for (let i = 0; i < start.length; i++) {
	const solution = graph.bfs(end, start[i]);
	if (solution?.distance < min) {
		min = solution.distance;
	}
}
console.log(min);