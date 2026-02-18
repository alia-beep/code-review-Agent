async function startReview() {
    const code = document.getElementById('codeInput').value;
    const output = document.getElementById('output');

    if (!code.trim()) return alert("Pehle code dalo!");

    output.style.display = "block";
    output.innerHTML = "🔍 Full Analysis in progress...";

    try {
        const response = await fetch('http://127.0.0.1:8000/review', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: code })
        });

        const data = await response.json();

        if (data.status === "success") {
            // 1. Runtime Header
            let html = `
                <div style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 15px; border-bottom: 1px solid #334155; padding-bottom: 8px;">
                    ⚡ Runtime: <span style="color: #fff; font-weight: bold;">${data.runtime}</span>
                </div>`;
            
            let errorsHtml = "";
            let suggestionsHtml = "";
            let isSuggestionSection = false;

           
            
            data.full_review.forEach(line => {
    
                let cleanLine = line.replace(/[*#`]/g, "").trim(); 
    
                if (!cleanLine || cleanLine === "---") return;

                if (cleanLine.toUpperCase().includes("ERROR:")) {
                    errorsHtml += `<div style="color: #f87171; background: #450a0a33; padding: 10px; border-radius: 5px; margin-bottom: 8px; border-left: 4px solid #f87171;">❌ ${cleanLine}</div>`;
                } else if (cleanLine.toUpperCase().includes("TIP:") || cleanLine.match(/^\d+\./)) {
      
                    suggestionsHtml += `<li style="color: #4ade80; margin-bottom: 10px; list-style: none;">✅ ${cleanLine.replace(/^TIP:\s*/i, "")}</li>`;
                }
            });

            // 2. Add Errors if any
            if (errorsHtml) {
                html += `<h4 style="color: #f87171; margin: 15px 0 10px 0;">Bugs Found:</h4>${errorsHtml}`;
            }

            // 3. Add Suggestions at the end
            if (suggestionsHtml) {
                html += `<h4 style="color: #4ade80; margin: 20px 0 10px 0;">Expert Suggestions:</h4>
                         <ul style="padding-left: 20px; list-style-type: none;">${suggestionsHtml}</ul>`;
            }
            
            output.innerHTML = html;
        }
    } catch (err) {
        output.innerHTML = "<span style='color:#f87171;'>Backend connection failed!</span>";
    }
}