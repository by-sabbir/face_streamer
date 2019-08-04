window.addEventListener('load', () => {
    let clock = document.getElementById('clock')
    let calendar = document.getElementById('date')
    let weekday = document.getElementById('weekday')
    let date = new Date()
    let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'Novermber', 'December']
    calendar.innerHTML = date.getUTCDate() + ' ' +
        months[date.getMonth()] + ', ' +
        date.getUTCFullYear()
    weekday.innerHTML = days[date.getDay()]
    clock.innerText = date.toLocaleString('en-US', {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    })
    progress()

})

function progress () {

}
