const redirecionamento = (complemento) => {
    let url = window.location.href.toString();
    window.location.href = url + complemento;
}
const goBack = () => { window.history.back() }