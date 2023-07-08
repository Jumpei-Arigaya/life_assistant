import Login from "@/features/Login";

const Page: () => Promise<JSX.Element> = async () => {
  return (
    <>
      <header className="py-4"></header>

      <main>
        <Login />
      </main>
    </>
  );
};

export default Page;
