/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch }) {
    const res = await fetch(`http://127.0.0.1:8000/tasks`);
    const item = await res.json();

    return {item};
}

// console.log(item)

// /** @type {import('./$types').Actions} */
// export const actions = {
//     default: async (event) => {
//         is_done = !is_done;
//         fetch("http://127.0.0.1:8000/task/" + id, {
//             method: 'PUT'
//         })   
//     }
// };