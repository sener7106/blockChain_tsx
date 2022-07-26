abstract class User {
  constructor(
    protected firstName: string,
    private lastName: string,
    public nickName: string,
  ) {}

  abstract getNickName(): void
}

class Players extends User {
  getNickName() {
    console.log(this.firstName)
  }
}

// private는 사용되지않음
const nico = new Players('nuco', 'las', '니꼬')

nico.getNickName()
