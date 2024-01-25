async function generatePDF(){
    document.getElementById("downloadBtn").innerHTML = "Currently downloading. Please wait...";

    try {
        // Download
        const printing = document.getElementById("printableArea");
        const doc = new jsPDF('p', 'pt');

        const canvas = await html2canvas(printing, {
            // Set whether images can be put onto your canvas
            //allowTaint: true,
            // useCORS: true,
            width: '100%'
        });
            
        // Convert your Canvas to a PNG
        doc.addImage(canvas.toDataURL("image/png"), 'PNG', 5, 5);

        doc.save("daniel_brunker_resume.pdf")

        // End of Download
        document.getElementById("downloadBtn").innerHTML = "<i class='fa-regular fa-print'></i>";
    } catch (error) {
        console.error("There was a problem generating your PDF: ", error)
    }
}