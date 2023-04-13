<p><a href="https://www.beecrowd.com.br/repository/UOJ_2602_en.html">beecrowd.com.br/repository/UOJ_2602_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2602</span>
                            <h1>Basic Select</h1>
                            <div>
                              <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>Your company is doing a survey of how many customers are registered in the states, however, lacked to raise the data of the state of the 'Rio Grande do Sul'.</p>
                            <p>Then, you must show the names of all customers whose state is 'RS'.</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>customers</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>id (PK)</td>
                          <td>numeric</td>
                        </tr>
                        <tr>
                          <td>name</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>street</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>city</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>state</td>
                          <td>char</td>
                        </tr>
                        <tr>
                          <td>credit_limit</td>
                          <td>number</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>customers</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>street</strong></td>
                  <td><strong>city</strong></td>
                  <td><strong>state</strong></td>
                  <td><strong>credit_limit</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Pedro Augusto da Rocha</td>
                  <td>Rua Pedro Carlos Hoffman</td>
                  <td>Porto Alegre</td>
                  <td>RS</td>
                  <td>700,00</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Antonio Carlos Mamel</td>
                  <td>Av. Pinheiros</td>
                  <td>Belo Horizonte</td>
                  <td>MG</td>
                  <td>3500,50</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Luiza Augusta Mhor</td>
                  <td>Rua Salto Grande</td>
                  <td>Niteroi</td>
                  <td>RJ</td>
                  <td>4000,00</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Jane Ester</td>
                  <td>Av 7 de setembro</td>
                  <td>Erechim</td>
                  <td>RS</td>
                  <td>800,00</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Marcos Antônio dos Santos</td>
                  <td>Av Farrapos</td>
                  <td>Porto Alegre</td>
                  <td>RS</td>
                  <td>4250,25</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>Pedro Augusto da Rocha</td>
        </tr>
        <tr>
          <td>Jane Ester</td>
        </tr>
        <tr>
          <td>Marcos Antônio dos Santos</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>