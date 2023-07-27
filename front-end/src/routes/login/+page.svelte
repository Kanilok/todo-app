<script>
    let username;
    let password;
    let repeated_password;

    async function logIn(){
        await fetch(`http://127.0.0.1:8000/users/login`, {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
            }).then(response => {
                if(!response.ok){
                    throw new Error("Network response was not ok");
                }
                return response.json()
            }).then(data => {
                localStorage.setItem("access_token", data.access_token)
            }).catch(error => {
                console.log(error)
            });

    }

    function signIn(){
        if(password == repeated_password){
            fetch("http://127.0.0.1:8000/users", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    username: username,
                    hashed_password: password
                })
            })
        }
    }

    function change(){
        const sign_form = document.getElementById("sign-in-form");
        const log_form = document.getElementById("log-in-form");

        sign_form.classList.toggle("hidden");
        log_form.classList.toggle("hidden");
    }

</script>

<div class="w-full max-w-xs mt-16 ml-auto mr-auto">
    <form id="log-in-form" class="bg-white shadow-xl rounded px-8 pt-6 pb-8 mb-4">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
          Username
        </label>
        <input bind:value={username} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline" type="text" placeholder="Username">
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
          Password
        </label>
        <input bind:value={password}  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:shadow-outline" type="password" placeholder="******************">
      </div>
      <div class="flex flex-col items-center ">
        <button class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-8 border border-blue-700 rounded" type="button" on:click={logIn}>
          Log In
        </button>
      </div>
      <p class="pt-8">Don't have an account? <button on:click={change} type="button" class="sign-change-form text-blue-700 font-semibold">Register</button></p>
    </form>

    <form id="sign-in-form" class="hidden bg-white shadow-xl rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input bind:value={username} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline" type="text" placeholder="Username">
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input bind:value={password}  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:shadow-outline" type="password" placeholder="******************">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Repeat Password
          </label>
          <input bind:value={repeated_password}  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:shadow-outline" type="password" placeholder="******************">
        </div>
        <div class="flex flex-col items-center ">
          <button class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-8 border border-blue-700 rounded" type="button" on:click={signIn}>
            Register
          </button>
        </div>
        <p class="pt-8">Go back to: <button on:click={change} type="button" class="log-change-form text-blue-700 font-semibold">Log In</button></p>
      </form>
  </div>