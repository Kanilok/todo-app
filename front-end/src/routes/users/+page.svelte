<script>
    import { onMount } from 'svelte';
    import { logStore } from "../store.js"
    import Users from "./Users.svelte"
    
    let is_fetched = false;
    const SERWER_URL = "http://127.0.0.1:8000";
    let users = [];

    async function fetchUsers(token) {

        await fetch(SERWER_URL + '/users/current', {
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            }).then(response => {
                if(!response.ok){
                    throw new Error("You are not logged in")
                }
                return response.json()
            }).then(data => {
                logStore.set({logged: true, username: data.username, admin: data.admin})
            }).catch(error => {
                console.error('Error fetching data:', error);
            });

        await fetch(SERWER_URL + '/users', {
            headers: {
                    Authorization: `Bearer ${token}`,
                }
        }).then(response => {
                if(!response.ok){
                    throw new Error("something went wrong")
                }
                return response.json()
            }).then(data => {
                for(let i in data){
                users.push({id: data[i].id, 
                            username: data[i].username,
                            verified: data[i].verified
                        })
                }
                is_fetched = true
            }).catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    onMount(() => {
        const token = localStorage.getItem("access_token")

        fetchUsers(token);
    });
    
</script>

{#if is_fetched}
    <Users {users} {SERWER_URL}/>
{/if}