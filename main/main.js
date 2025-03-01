async function generateScript() {
    // 取得用戶選擇的操作
    const operation = document.getElementById("operation").value;

    try {
        // 向伺服器發送請求
        const response = await fetch("/generate_script", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ operation })
        });

        // 處理伺服器回應
        const data = await response.json();
        if (data.error) {
            alert("發生錯誤：" + data.error);
        } else {
            // 顯示產生的 Python 代碼
            document.getElementById("script_output").innerText = data.script;
            // 顯示下載連結
            document.getElementById("download_link").style.display = "block";
        }
    } catch (error) {
        alert("請求失敗：" + error.message);
    }
}