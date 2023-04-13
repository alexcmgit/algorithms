<p><a href="https://www.beecrowd.com.br/repository/UOJ_2744_en.html">beecrowd.com.br/repository/UOJ_2744_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2744 </span>
                            <h1>Passwords</h1>
                            <div>
                              <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>You were hired to be the consultant for a company. Analyzing the database, you noticed that the passwords are stored as text files and, as everyone knows, this is a terrible security practice as they are not encrypted.</p>
                            <p>Therefore you must convert every password to the MD5 format. Show the client <b>id</b>, the password before conversion and the new MD5.</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>account</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>id (PK)</td>
                          <td>integer</td>
                        </tr>
                        <tr>
                          <td>name</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>login</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>password</td>
                          <td>varchar</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>account</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>login</strong></td>
                  <td><strong>password</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Joyce P. Parry</td>
                  <td>Promeraw</td>
                  <td>noh1Oozei</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Michael T. Gonzalez</td>
                  <td>Phers1942</td>
                  <td>Iath3see9bi</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Heather W. Lawless</td>
                  <td>Hankicht</td>
                  <td>diShono4</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Otis C. Hitt</td>
                  <td>Conalothe</td>
                  <td>zooFohH7w</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Roger N. Brownfield</td>
                  <td>Worseente</td>
                  <td>fah7ohNg</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>id</strong></td>
          <td><strong>password</strong></td>
          <td><strong>MD5</strong></td>
        </tr>
        <tr>
          <td>1</td>
          <td>noh1Oozei</td>
          <td>b67ed42ced0e0a19ce7ed904bb94b607</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Iath3see9bi</td>
          <td>66877b2da87fb09af3f5602f31c6d35c</td>
        </tr>
        <tr>
          <td>3</td>
          <td>diShono4</td>
          <td>d19c9be4c00c683a4688948b81eb2a1d</td>
        </tr>
        <tr>
          <td>4</td>
          <td>zooFohH7w</td>
          <td>202b76ed4a556fdbf409505a8023695e</td>
        </tr>
        <tr>
          <td>5</td>
          <td>fah7ohNg</td>
          <td>05b3dccaa70f228f1bedc7a285e50d9d</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>