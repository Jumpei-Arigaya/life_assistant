import SignIn from "@/features/accounts/components/SiginIn";

const Page: () => Promise<JSX.Element> = async () => {
  return (
    <>
      <header className="py-4"></header>

      <main>
        <SignIn />
      </main>
    </>
  );
};

export default Page;
