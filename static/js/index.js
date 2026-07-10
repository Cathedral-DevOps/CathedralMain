document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".item");

  if (items.length === 0) {
    console.warn("GSAP: no .item elements found");
    return;
  }

  gsap.fromTo(
    items,
    { opacity: 0, visibility: "hidden", y: 30 },
    {
      opacity: 1,
      visibility: "visible",
      y: 0,
      duration: 0.8,
      ease: "power1.out",
      stagger: 0.15,
      overwrite: "auto",
    }
  );
  
});
