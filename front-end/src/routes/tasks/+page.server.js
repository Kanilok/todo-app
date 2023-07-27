/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch }) {
    // console.log(localStorage.getItem("access_token"))
    const res = await fetch(`http://127.0.0.1:8000/tasks`);
    const item = await res.json();

    return {item};
}